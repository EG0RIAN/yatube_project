from django.urls import path

from . import views
app_name = "posts"
urlpatterns = [
    path('', views.index, name='index'),
    path(
        'group/<int:pk>',
        views.group_posts,
        name='group_list'
    ),
]