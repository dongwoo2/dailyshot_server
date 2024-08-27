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

# update 위주
class SellCountData(models.Model): # update 위주의 쿼리가 들어가야 할 것
    sell_alcol_id = models.IntegerField() # 팔린거 id
    sell_alcol_name = models.CharField(max_length=100, default='기타')
    sell_date = models.DateField() # 팔린 날
    sell_count = models.FloatField() # 팔린 양


# SellData에 있는 데이터들 업데이트 될 때마다 상세 기록 뭐가 업데이트 되고 그랬는지

# 근데 날짜도 있어야할듯 index 용으로다가
class SellData_Check(models.Model):
    sell_alcol_id = models.IntegerField() # 일단 selldata랑 id값 같아야하고
    sell_data = models.DateField() # 팔린 날 검색할 index용은 있어야 함
    sell_Sequence = models.IntegerField() # 업데이트 기록 최고
    sell_status = models.IntegerField() # 상태 기록

