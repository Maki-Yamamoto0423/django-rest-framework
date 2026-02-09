from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# ---------------------------------------------
# Snippet List
# URL: /snippets/
# Methods: GET, POST
# ---------------------------------------------
class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        """
        GET /snippets/
        全てのスニペットを取得して返す
        """
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        POST /snippets/
        新しいスニペットを作成
        """
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------------
# Snippet Detail
# URL: /snippets/<int:pk>/
# Methods: GET, PUT, DELETE
# ---------------------------------------------
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a code snippet instance.
    """

    def get_object(self, pk):
        """
        pk からスニペットを取得。
        存在しなければ 404 を返す。
        """
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        GET /snippets/<pk>/
        指定IDのスニペットを取得
        """
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        PUT /snippets/<pk>/
        指定IDのスニペットを更新
        """
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        DELETE /snippets/<pk>/
        指定IDのスニペットを削除
        """
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)