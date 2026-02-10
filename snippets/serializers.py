from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet


# =================================================
# Snippet Serializer
# 関連を「ID」ではなく「URL」で表現する
# =================================================
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight",
        format="html"
    )

    class Meta:
        model = Snippet
        # url フィールドは HyperlinkedModelSerializer で必須
        fields = [
            "url",
            "id",
            "highlight",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
        ]


# =================================================
# User Serializer
# User → Snippet の関連もリンクで表現
# =================================================
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="snippet-detail",
        read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]