from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from map.models import Alcolshop
from shop.models import AllShop, ShopDrinks_Count, DrinkSalesRate
from alcoldrinks.models import AlcolDrinks
import json
from rest_framework.response import Response
# Create your views here.

class Show(APIView):
    def get(self, request):
        return render(request, "shop/show.html")

class ShopJoin(APIView):
    def get(self, request):
        return render(request, "shop/shopjoin.html")

    def post(self, request):
        # TODO 입점
        name = request.data.get('name', None)
        location = request.data.get('location', None)
        latitude = request.data.get('latitude', None)
        longitude = request.data.get('longitude', None)
        alcolshoptype = request.data.get('alcolshoptype', None)

        if Alcolshop.objects.filter(name=name, location=location).exists():
            return JsonResponse({'status': 'error', 'message': '중복된 데이터입니다.'}, status=400)
        else:
            Alcolshop.objects.create(name=name,
                                location=location,
                                latitude=latitude,
                                longitude=longitude,
                                alcolshoptype=alcolshoptype)

            AllShop.objects.create(name=name,
                                   location=location,
                                   alcolshoptype=alcolshoptype)
            return JsonResponse({'status': 'success', 'message': '데이터가 성공적으로 생성되었습니다.'})

        #return Response(status=200)



# def show(request):
#     return render(request, 'shop/show.html')
class ShopAlcolDetail(APIView): # 전체 가게들이 보이게 한 다음에 가게마다 클릭해서 가게를 볼 수 있게
    def get(self, request):

        #shopid = AllShop.objects.filter(id=id)
        shop = AllShop.objects.all()
        alcoldrinks = AlcolDrinks.objects.all()
        return render(request,'shop/allshopdrinks.html', context={'shop':shop, 'alcoldrinks':alcoldrinks})

# class ShopDrinks(APIView): # 하나 더 만들어야함 이거는 1개만 조회가능 전체조회하는 API만들어야함
#     def get(self, request):
#         drink = ShopDrinks_Count.objects.filter(id=id)


class DrinkSalesRate(APIView): # 판매 정산
    def get(self, request):
        drinkrate = DrinkSalesRate.objects.get(id=id)
        shopname = AllShop.objects.filter(id=id) # 이름 구하기용
        alcoldrinks = AlcolDrinks.objects.filter(id=id)
        return render(request,'shop/shopsales.html', context={'drinkrate':drinkrate,'shopname':shopname,'alcoldrinks':alcoldrinks})









