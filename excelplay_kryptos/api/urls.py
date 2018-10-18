from django.urls import path
from . import views

urlpatterns = [
    path('ask', views.ask),
    path('answer', views.answer),
]
