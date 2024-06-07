from django.urls import path

urlspatterns = [
    path('products/', ProductListView.as_view()),
]