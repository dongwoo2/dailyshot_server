from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password
# Create your views here.


class Join(APIView):
    def get(self, request):
        return render(request, 'user/join.html')

    def post(self, request):
        # TODO 회원가입
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)


        # password 는 민감정보 이기 떄문에 암호화해서 넣어야함
        # password 단방향 암호화를 주로 사용함
        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_img='default_profile.jpg')

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first() # 어차피 유니크이기 때문에 하나만 옴 그렇지만 first를 붙이지 않으면 리스트 형태로 넘어옴 그러면 for문 써서 한 번 귀찮게 데이터 가져와야함

      #  if user in None:
          #  return Response(status=400, data=dict(message='회원 정보가 잘못되었습니다.'))

        if user.check_password(password):
            # 로그인을 했다 . 세션 or 쿠키에 넣는다.
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data=dict(message='회원 정보가 잘못되었습니다.'))