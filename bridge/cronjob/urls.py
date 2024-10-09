from django.urls import path
from . import views



urlpatterns = [
    path('', views.SyncView.as_view(), name=''),
]