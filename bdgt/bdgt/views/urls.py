from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("bdgt/", include("bdgt.urls")),
    path(r"^admin/", include(admin.site.urls)),
]