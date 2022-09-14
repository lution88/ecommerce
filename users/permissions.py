import os
import jwt

from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomPermission(BasePermission):
    """유저 권한"""

    def has_permission(self, request, view):
        print(request.method, request.user)
        if request.method in SAFE_METHODS:
            return True
        else:
            token = request.headers.get("Authorization")
            payload = jwt.decode(
                token, os.environ.get("SECRET_KEY"), os.environ.get("ALGORITHM")
            )
            print(os.environ.get("SECRET_KEY"), os.environ.get("ALGORITHM"))
            token_user = payload.get("user_id")
            print(token_user)
        return

    def has_object_permission(self, request, view, obj):
        print(request.method, request.user)
        if request.method in SAFE_METHODS:
            return True
        else:
            token = request.headers.get("Authorization")
            payload = jwt.decode(
                token, os.environ.get("SECRET_KEY"), os.environ.get("ALGORITHM")
            )
            token_user = payload.get("user_id")

            return obj.order.user.id == token_user
