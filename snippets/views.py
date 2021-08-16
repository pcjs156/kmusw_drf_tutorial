from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    모든 code snippet의 목록을 반환하거나, 새 snippet을 생성함
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    code snippet의 조회, 수정, 삭제를 수행함
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
