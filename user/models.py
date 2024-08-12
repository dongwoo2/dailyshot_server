from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models

# Create your models here.


# user 커스텀 하자
class User(AbstractBaseUser): # AbstractBaseUser 를 상속받으면 그게 user 필드가 된다.
    """
    유저 닉네임 - 화면에 표기되는 이름
    유저 이름 - 실제 사용자 이름
    유저 이메일 - 회원가입할 때 사용하는 아이디
    유저 비밀번호는 - 디폴트로 쓰자
    """
    profile_img = models.TextField() # 프로필 이미지
    nickname = models.CharField(max_length = 24, unique = True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname' # 실제로 유저를 선택했을 때 어떤 필드를 쓰게할 것 인가
    class Meta:
        db_table = 'User'
