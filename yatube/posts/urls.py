from django.urls import path

from . import views
app_name = "posts"
urlpatterns = [
    path('', views.index),
    path(
        'group/<int:pk>',
        views.group_posts
    ),
]