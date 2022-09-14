from django.urls import path

from . import views
from .views import ProductAPIView, ProductsAPIView

urlpatterns = [
    path("", ProductsAPIView.as_view()),
    path("<int:product_id>/", ProductAPIView.as_view())
]
