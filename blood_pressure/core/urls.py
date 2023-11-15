from django.urls import path
from . import views

app_name="core"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("filter/", views.FilteredIndex.as_view(), name="filteredIndex"),
]