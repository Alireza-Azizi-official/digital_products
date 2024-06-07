from django.urls import path
from .views import ProductListView
urlspatterns = [
    path('products/', ProductListView.as_view()),
]