from django.urls import path
from . import views


urlpatterns = [
    path('ask', views.ask),
    path('answer', views.answer),
    path('ranklist', views.leaderboard),
    path('test', views.test_session),
    path('myrank', views.myrank)
]
