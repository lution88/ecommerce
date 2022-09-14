from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    admin 계정은 쓰기, 수정, 삭제 가능
    일반 유저는 조회만 가능
    """
    SAFE_METHOD = ("GET",)
    message = "접근 권한이 없습니다."

    def has_permission(self, request, view):
        user = request.user
        if request.method in self.SAFE_METHOD or user.is_admin:
            return True

        return False