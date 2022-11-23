
from django.urls import path
from . import views

urlpatterns = [
    path("item/<int:pk>/", views.item, name="item"),
    path("buy/<int:pk>/", views.buy, name="buy"),
    path("cancel/", views.cancel, name="cancel"),
    path("success/", views.success, name="success"),
]