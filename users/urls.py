from django.urls import path
from .views import UserListApiView, UserAPIView

urlpatterns = [
    path("", UserListApiView.as_view()),
    path("signup/", UserAPIView.as_view()),
]
