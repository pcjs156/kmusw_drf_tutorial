from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# 라우터 생성 및 viewset 등록
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# 라우터에 의해 자동으로 API URL이 결정되었음
urlpatterns = [
    path('', include(router.urls)),
]
