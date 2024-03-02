from django.urls import path
from . import views

urlpatterns = [
    path("", views.UrlConversionView.as_view(), name="conversion-create")
]
