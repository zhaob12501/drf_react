from django.urls import path
from . import views

urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view()),
    path('api/lead/<int:pk>/', views.LeadUpdate.as_view()),
]
