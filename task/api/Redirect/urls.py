from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_to_original, name="redirect-to-original")
]