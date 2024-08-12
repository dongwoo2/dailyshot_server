from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User


class Main(APIView):
    def get(self, request):
        #print('로그인한 사용자 : ', request.session['email'])

#        email = request.session['email']

        if 'email' in request.session:
            email = request.session['email']
        else:
            # 세션에 email이 없을 때의 처리
            email = None  # 또는 적절한 기본값 설정

        user = User.objects.filter(email=email).first()
        if email is None:
            return render(request, 'user/login.html')

        if user is None: # 이메일은 있지만 우리 사용자가 아닐 경우 그래도 로그인 다시해
            return render(request, 'user/login.html')


        return render(request, "main.html", context={'user': user})

    def post(self, request):
        print("포스트로 호출")
        return render(request, "main.html")