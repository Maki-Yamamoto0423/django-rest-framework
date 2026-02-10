from django.contrib.auth.models import User

from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly


# =================================================
# URL: /
# Methods: GET
# API 全体の入口となるエンドポイント
# =================================================
@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        "users": reverse("user-list", request=request, format=format),
        "snippets": reverse("snippet-list", request=request, format=format),
    })


# ---------------------------------------------
# Snippet List
# URL: /snippets/
# Methods: GET, POST
# ---------------------------------------------
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        # Snippet 作成時にログインユーザーを owner に設定
        serializer.save(owner=self.request.user)


# ---------------------------------------------
# Snippet Detail
# URL: /snippets/<int:pk>/
# Methods: GET, PUT, DELETE
# ---------------------------------------------
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsOwnerOrReadOnly]


# =================================================
# URL: /snippets/<int:pk>/highlight/
# Methods: GET
# JSONではなく HTML（シンタックスハイライト済み）を返す
# =================================================
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


# ---------------------------------------------
# User List
# URL: /users/
# Methods: GET
# ---------------------------------------------
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ---------------------------------------------
# User Detail
# URL: /users/<int:pk>/
# Methods: GET
# ---------------------------------------------
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer