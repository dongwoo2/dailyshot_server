from django.db import models

# Create your models here.
class SellData(models.Model):
    sell_alcol_id = models.IntegerField() # 팔린 술 id
    sell_date = models.DateField() # 팔린날
    sell_time = models.TimeField() #
    sell_price = models.FloatField()
    sell_amount = models.FloatField()
    sell_status = models.IntegerField() # 환불, 완료 이런 상태 값 넣을 곳
    sell_comment = models.TextField()

class SellCountData(models.Model): # update 위주의 쿼리가 들어가야 할 것
    sell_alcol_id = models.IntegerField() # 팔린거 id
    sell_date = models.DateField() # 팔린 날
    sell_count = models.FloatField() # 팔린 양
