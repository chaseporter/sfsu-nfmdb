from django.urls import path
from . import views 

urlpatterns = [
    path("get_data/", views.get_nfmdb_data),
    path("", views.get_nfmdb_data)
]