from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.test),
    path('ask/', views.ask),
    path('answer/', views.answer),
]