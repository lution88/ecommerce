from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import UserListApiView, UserAPIView, SignInAPIView

urlpatterns = [
    # access token 발급
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh token 발급
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("", UserListApiView.as_view()),
    path("signup/", UserAPIView.as_view()),
    path("signin/", SignInAPIView.as_view()),
    path("<int:user_id>/", UserAPIView.as_view()),
]
