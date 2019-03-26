from django.urls import include, path, re_path
from .views import CreateUser

urlpatterns = [
    path('users/', CreateUser.as_view(), name="CreateUser"),
]