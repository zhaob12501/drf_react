from django.urls import path
from . import views

urlpatterns = [
    path('goods/', views.GoodsListCreate.as_view()),
]
