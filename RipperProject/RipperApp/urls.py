from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('', views.home_view, name='index'),
    path('edit/', views.song_edit_view, name='edit'),
    path('next/', views.next_page),
    path('home/', views.home_view),
    path('about/', views.about_view),
    path('download/', views.download_view)
    # path('list/', views.list, name='list'),
    ]

