from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import re  # 정규 표현식을 사용하기 위한 모듈
# Create your views here.


class Join(APIView):
    def get(self, request):
        if request.session.get('email'):
            messages.warning(request, '이미 로그인 되어있습니다.')
            return redirect('/main')

        return render(request, 'user/join.html')

    def post(self, request):
        # TODO 회원가입
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        # 이메일 중복 체크
        if User.objects.filter(email=email).exists():
            return Response(status=400, data=dict(message='이미 사용 중인 이메일입니다.'))

        # 닉네임 중복 체크
        if User.objects.filter(nickname=nickname).exists():
            return Response(status=400, data=dict(message='이미 사용 중인 닉네임입니다.'))

        # 비밀번호 유효성 검사
        if not self.is_valid_password(password):
            return Response(status=400, data=dict(message='비밀번호는 8자리 이상이어야 하며, 영어와 숫자가 모두 포함되어야 합니다.'))




        # password 는 민감정보 이기 떄문에 암호화해서 넣어야함
        # password 단방향 암호화를 주로 사용함
        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_img='default_profile.jpg')

        return Response(status=200)

    def is_valid_password(self, password):
        # 비밀번호가 8자리 이상인지 확인
        if len(password) < 8:
            return False
        # 비밀번호에 영어와 숫자가 모두 포함되어 있는지 확인
        if not re.search(r'[A-Za-z]', password) or not re.search(r'[0-9]', password):
            return False
        return True

class Login(APIView):
    def get(self, request):
        if request.session.get('email'):
            messages.warning(request, '이미 로그인 되어있습니다.')
            return redirect('/main')

        return render(request, 'user/login.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first() # 어차피 유니크이기 때문에 하나만 옴 그렇지만 first를 붙이지 않으면 리스트 형태로 넘어옴 그러면 for문 써서 한 번 귀찮게 데이터 가져와야함

        if user is None:
            return Response(status=400, data=dict(message='회원 정보가 잘못되었습니다.'))

        if user.check_password(password):
            # 로그인을 했다 . 세션 or 쿠키에 넣는다.
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message='회원 정보가 잘못되었습니다.'))

class Logout(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, 'user/login.html')