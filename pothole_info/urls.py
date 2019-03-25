from django.urls import include, path, re_path
from .views import PotholeList, NearbyPotholeList, PotholeView

urlpatterns = [
    path('view/<int:pk>/', PotholeList.as_view(), name="PotholeList"),
    path('view/', PotholeView.as_view(), name="PotholeView"),
    re_path(r'^nearby/(?P<lat>[0-9]*[.]{0,1}[0-9]*)/(?P<long>[0-9]*[.]{0,1}[0-9]*)', NearbyPotholeList.as_view(), name="NearbyPotholeList"),
]