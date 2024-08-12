from django.urls import path
from .views import Show, ShopJoin, ShopAlcolDetail, DrinkSalesRate

app_name = 'shop'

urlpatterns = [
    path('show/', Show.as_view(), name='show'),
    path('shopjoin', ShopJoin.as_view(), name='shopjoin'),
    path('shopAlcolDetail', ShopAlcolDetail.as_view(), name='shopAlcolDetail'),
    path('shopsalesrate/<int:id>/', DrinkSalesRate.as_view(), name='shopsalesrate')
]