from django.urls import path

from . import views
from .views import KakaoMapView, KeywordSearch

app_name = 'map'

urlpatterns = [
    #path('', views.index, name='index'),
    path('KakaoMap', KakaoMapView.as_view(), name='kakaomap'),
    path('KeywordSearch', KeywordSearch.as_view(), name='keywordsearch'),
]