from django.urls import path
from . import views

urlpatterns = [
    path("", views.UrlConversionCreate.as_view(), name="conversion-create")
]
