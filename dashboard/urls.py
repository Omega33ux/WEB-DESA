from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("potensi/slug:slug/", views.potensi_detail, name="potensi_detail"),
    path("berita/slug:slug/", views.berita_detail, name="berita_detail"),
    path("rt-rw/", views.rt_rw, name="rt_rw"),
]