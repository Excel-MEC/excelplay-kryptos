from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ask', views.ask),
    path('answer', views.answer),
    path('ranklist', views.leaderboard),
    path('test', views.test_session),
    path('myrank', views.myrank)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
