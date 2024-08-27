from django.db import models

# Create your models here.

'''
erp_selldata 테이블 id 값 컬럼 정의

예) 202408271644550101000001

앞에는 날짜가 들어가고 뒤에는 술 종류 넘버가 들어간다

20240827164455 앞에 14자리는 날짜

0101 뒤에 4자리는 술 종류 01 위스키 01 버번 이렇게

000001 뒤에 6자리는 오늘 주문이 들어간 술 
=================================================
sell_status 컬럼 정리

01 - 주문 완료
02 - 배송중
03 - 배송완료
04 - 환불
05 - 분실
'''
class SellData(models.Model):
    sell_alcol_id = models.IntegerField() # 팔린 술 id
    sell_price = models.FloatField()
    sell_amount = models.FloatField()
    sell_status = models.IntegerField() # 환불, 완료 이런 상태 값 넣을 곳
    sell_comment = models.TextField()

class SellCountData(models.Model): # update 위주의 쿼리가 들어가야 할 것
    sell_alcol_id = models.IntegerField() # 팔린거 id
    sell_date = models.DateField() # 팔
    sell_count = models.FloatField() # 팔린 양
