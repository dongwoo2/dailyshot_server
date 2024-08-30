from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User

#
from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from alcoldrinks.models import AlcolDrinks
#
class Main(APIView):
    def get(self, request):
        # 세션에서 이메일을 가져옵니다.
        email = request.session.get('email',None)  # get() 메소드를 사용하여 KeyError 방지

        # 이메일이 없으면 로그인 페이지로 리다이렉트
        if email is None:
            return render(request, 'user/login.html')

        # 이메일이 있다면 사용자 정보를 가져옵니다.
        user = User.objects.filter(email=email).first()

        # 사용자가 존재하지 않으면 로그인 페이지로 리다이렉트
        if user is None:
            return render(request, 'user/login.html')

        feed_object_list = AlcolDrinks.objects.all().order_by('-id')
        feed_list = []
        for feed in feed_object_list:
            feed_list.append(dict(
                id=feed.id,
                name=feed.name,
                image=feed.image,
                alcol_type=feed.alcol_type,
                drink_type=feed.drink_type,
                information=feed.information,
            ))
        # 사용자 정보가 존재하면 메인 페이지를 렌더링합니다.
        return render(request, "main.html", context={'user': user, 'feed_list': feed_list})

    def post(self, request):
        print("포스트로 호출")
        return render(request, "main.html")


