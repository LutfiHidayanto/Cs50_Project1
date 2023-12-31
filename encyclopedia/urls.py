from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newPage, name="new-page"),
    path("editpage/<str:title>", views.editPage, name="edit"),
    path("random/", views.random, name="random")
]
