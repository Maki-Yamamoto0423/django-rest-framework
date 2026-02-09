from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

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