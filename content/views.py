from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User

#
from django.shortcuts import render
from rest_framework.views import APIView
from user.models import User
from alcoldrinks.models import AlcolDrinks
from .models import Reply, Like, Bookmark


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
            reply_object_list = Reply.objects.filter(feed_id=feed.id) # 피드 id를 통해 댓글 목록 가져오고
            reply_list = [] # 리스트 만들고
            for reply in reply_object_list: # 만들어진 리스트에 reply로 뽑아내고
                user = User.objects.filter(email=email).first() # 사용자 뽑아내고
                reply_list.append(dict( # 더한다
                    reply_text=reply.reply_text, # reply_text에 reply.reply_text 내용을 대입한다. 맞는데?
                    nickname=user.nickname, # nickname에 user.nickname 넣고
                ))
            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count() # like_count
            is_liked = Like.objects.filter(feed_id=feed.id, email=email,
                                           is_like=True).exists()
            is_marked = Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()

            feed_list.append(dict(
                    id=feed.id,
                    name=feed.name,
                    image=feed.image,
                    alcol_type=feed.alcol_type,
                    drink_type=feed.drink_type,
                    information=feed.information,
                    like_count=like_count,
                    nickname=user.nickname, # 실시간 데이터 반영
                    reply_list=reply_list,
                    is_liked=is_liked,
                    is_marked=is_marked,

                ))
        # 사용자 정보가 존재하면 메인 페이지를 렌더링합니다.
        return render(request, "main.html", context={'user': user, 'feed_list': feed_list})

    def post(self, request):
        print("포스트로 호출")
        return render(request, "main.html")


# 프로필에 내가 북마크하거나 좋아요 한 Alcoldrinks 객체가 나와야함
# 내가 글을 올리는 기능은 단순히 운영자가 올리는 것임 지금은 영역 구분이 안되어있으나 구분을 해야함
#

class Profile(APIView):
    def get(self, request):
        email = request.session.get('email',None)

        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")
        # 내가 좋아요 누른 애들
        # 당연히 email = email 내가 눌렀단 증거가 있어야 하고
        # 어떤 피드에 좋아요 눌렀는지 확인하고
        like_list = list(Like.objects.filter(email=email,is_like=True).values_list('alcoldrinks_id', flat=True))
        like_feed_list = AlcolDrinks.objects.filter(id__in=like_list)



class ToggleLike(APIView):
    def post(self, request):
        alcoldrinks_id = request.data.get('alcoldrinks_id', None)





