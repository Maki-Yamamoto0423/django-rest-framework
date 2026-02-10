from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # 読み取り系は誰でもOK
        if request.method in permissions.SAFE_METHODS:
            return True

        # 書き込みは owner のみ
        return obj.owner == request.user