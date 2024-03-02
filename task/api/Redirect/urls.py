from django.urls import path
from . import views

urlpatterns = [
    path("", views.RedirectView.as_view(), name="redirect-to-original")
]
