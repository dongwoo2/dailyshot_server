from django.urls import path

from .views import Profile, ToggleLike, ToggleBookmark

app_name = 'content'

urlpatterns = [
    #path('', views.index, name='index'),
    path('profile', Profile.as_view(), name='profile'),
    path('like', ToggleLike.as_view(), name='like'),
    path('bookmark', ToggleBookmark.as_view(), name='bookmark'),
]