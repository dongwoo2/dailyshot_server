from django.db import models

# Create your models here.
class AlcolDrinks(models.Model):

    ALCOL_TYPE_CHOICES = { # 술 종류
        ('Whisky','위스키'),
        ('Soju','소주'),
        ('Sake','사케'),
        ('Wine','와인'),
        ('Beer','맥주'),
        ('Other', '기타'),
    }
    DRINK_TYPE_CHOICES = [ # 술 세부 종류
        ('Bourbon', '버번'),
        ('Scotch', '스카치'),
        ('Soju','소주'),
        ('Sake', '사케'),
        ('Red Wine', '레드와인'),
        ('White Wine', '화이트와인'),
        ('Lager', '라거'),
        ('ALE', '에일'),
        ('Other', '기타'),
    ]



    name = models.CharField(max_length=70) # 술 이름
    inventory = models.CharField(max_length=70) # 재고
    price = models.CharField(max_length=70) # 가격
    image = models.TextField(blank=True)
    information = models.TextField(blank=True)
    alcol_type = models.CharField(max_length=20, choices= ALCOL_TYPE_CHOICES, default='Other')
    drink_type = models.CharField(max_length=20, choices= DRINK_TYPE_CHOICES, default='Other')

