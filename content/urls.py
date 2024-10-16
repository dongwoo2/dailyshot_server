from django.urls import path

from .views import Profile

app_name = 'content'

urlpatterns = [
    #path('', views.index, name='index'),
    path('profile', Profile.as_view(), name='profile'),
]