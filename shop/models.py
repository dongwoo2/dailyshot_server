from django.db import models
from alcoldrinks.models import AlcolDrinks
# Create your models here.

class AllShop(models.Model):
    CHOICE = {
        ('patner','파트너'), ('store','스토어')
    }
    name = models.CharField(max_length=100);
    location = models.CharField(max_length=100);
    alcolshoptype = models.CharField(max_length=20, choices=CHOICE, default='patner')

class Filter(models.Model):
    patner = models.BooleanField(default='True')
    store = models.BooleanField(default='True')
    
class ShopDrinks_Count(models.Model):
    shop = models.ForeignKey(AllShop, on_delete=models.CASCADE) # 가게 외래키랑 연결
    drinks_id = models.ForeignKey(AlcolDrinks, on_delete=models.CASCADE) # 술 아이디랑 연결
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

class DrinkSalesRate(models.Model):
    shop = models.ForeignKey(AllShop, on_delete=models.CASCADE) # 가게
    drinks_id = models.ForeignKey(AlcolDrinks, on_delete=models.CASCADE) # 술 id
    sales_rate_count = models.IntegerField(default=0) # 판매양
    price = models.IntegerField(default=0) # 가격
    date = models.DateField(auto_now_add=True)