from django.db import models

# Create your models here.
class AlcolDrinks(models.Model):

    ALCOL_TYPE_CHOICES = { # 술 종류
        ('Whisky','위스키'), # 01
        ('Soju','소주'), # 02
        ('Sake','사케'), # 03
        ('Wine','와인'),# 04
        ('Beer','맥주'), # 05
        ('Other', '기타'), # 06
    }
    DRINK_TYPE_CHOICES = [ # 술 세부 종류
        ('Bourbon', '버번'), # 01
        ('Scotch', '스카치'), # 02
        ('Soju','소주'), # 03
        ('Sake', '사케'), # 04
        ('Red Wine', '레드와인'), # 05
        ('White Wine', '화이트와인'), # 06
        ('Lager', '라거'), # 07
        ('ALE', '에일'), # 08
        ('Other', '기타'), # 09
    ]



    name = models.CharField(max_length=70) # 술 이름
    inventory = models.CharField(max_length=70) # 재고
    price = models.CharField(max_length=70) # 가격
    image = models.TextField(blank=True)
    information = models.TextField(blank=True)
    alcol_type = models.CharField(max_length=20, choices= ALCOL_TYPE_CHOICES, default='Other')
    drink_type = models.CharField(max_length=20, choices= DRINK_TYPE_CHOICES, default='Other')

