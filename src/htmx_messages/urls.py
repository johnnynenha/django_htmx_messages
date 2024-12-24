from django.urls import path

from .views import htmx_message

urlpatterns = [
    path("htmx_message/", htmx_message, name="htmx_message"),
]
