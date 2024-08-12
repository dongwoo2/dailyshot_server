from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Alcolshop, Filter
from shop.models import AllShop
from .forms import FilterForm
import geocoder


class KakaoMapView(View):
    def get(self, request):
        alcolshops = Alcolshop.objects.all()
        coordinate = geocoder.ip('me').latlng

        # Filter 객체가 없는 경우 기본값으로 생성
        if not Filter.objects.exists():
            Filter.objects.create(patner=True, store=True)  # 기본값 설정

        option = get_object_or_404(Filter)

        form = FilterForm(instance=option)

        if option.patner == False:
            alcolshops = alcolshops.exclude(alcolshoptype='patner')
        if option.store == False:
            alcolshops = alcolshops.exclude(alcolshoptype='store')

        return render(request, "map/kakaomap.html", {'alcolshops': alcolshops, 'form': form, 'coordinate': coordinate})

    def post(self, request):
        option = get_object_or_404(Filter)
        form = FilterForm(request.POST, instance=option)
        if form.is_valid():
            option = form.save(commit=False)
            option.save()
            return redirect('map:kakaomap')

        alcolshops = Alcolshop.objects.all()
        coordinate = geocoder.ip('me').latlng

        if option.patner == False:
            alcolshops = alcolshops.exclude(alcolshoptype='patner')
        if option.store == False:
            alcolshops = alcolshops.exclude(alcolshoptype='store')

        return render(request, "map/kakaomap.html", {'alcolshops': alcolshops, 'form': form, 'coordinate': coordinate})


# 이름만 필요해서 q 모듈 아직 필요없음
# class Alcolshop(models.Model): name
class KeywordSearch(APIView):
    def get(self, request):
        alcolshop_list = Alcolshop.objects.all()
        keywords = request.GET.get('keywords', '')
        keywords_list = []
        print("keywords : ", keywords)
        if keywords:
            keywords_list = alcolshop_list.filter(name__icontains=keywords)
            print("검색된 결과 : ", keywords_list)  # 필터링된 결과 출력
        if not keywords_list:
            return Response({'message': '검색 결과가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        # JSON 응답으로 반환
        results = [{'name': alcolshop.name, 'latitude': alcolshop.latitude, 'longitude': alcolshop.longitude}for
                   alcolshop in keywords_list]
        return Response(results, status=status.HTTP_200_OK)

# urls.py에 다음과 같이 추가:
# from .views import KakaoMapView
# urlpatterns = [
#     path('map/KakaoMap', KakaoMapView.as_view(), name='kakaomap')
# ]
