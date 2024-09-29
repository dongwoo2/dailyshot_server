from django.urls import path

from .views import Profile



urlpatterns = [
    #path('', views.index, name='index'),
    path('profile', Profile.as_view(), name='profile'),
]