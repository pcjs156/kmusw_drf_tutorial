from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체의 소유자만 수정할 수 있도록 하기 위한 custom permission
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 요청에 대해 허용되므로, 항상 GET/HEAD/OPTIONS는 허용함
        if request.method in permissions.SAFE_METHODS:
            return True

        # snippet의 소유자에게만 쓰기 권한이 부여됨
        return obj.owner == request.user
