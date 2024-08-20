from django.test import TestCase
from django.contrib.auth.hashers import make_password
from user.models import User


# Create your tests here.
class UserTest(TestCase):

    @classmethod # 먼저 실행됨 미리 데이터 셋팅 해놓는거
    def setUpTestData(cls):
        User.objects.create(
            email='test@naver.com',
            nickname='test_nick',
            name='test_name',
            password=make_password('PASSWORD'),
            profile_img='default_profile.png',
        )

    # 정상적으로 회원가입 API 호출했을 떄 200이 나오나? 체크하는 함수
    def test_join(self):
        response = self.client.post('/user/join', data=dict(
            email='test2@naver.com',
            nickname='test_nickname',
            name='test_name',
            password='PASSWORD',
        ))
        self.assertEqual(response.status_code, 200) # 이건 API가 제대로 호출됐는지 테스트 한거고
        #실제로 개발데이터베이스에 있는 데이터가 같은지 체크할려면 밑에 꺼 쓰기
        user = User.objects.filter(email='test@naver.com').first()

        self.assertEqual(user.nickname, 'test_nick')
        self.assertEqual(user.name, 'test_name')
        self.assertTrue(user.check_password('PASSWORD'), True)


    def test_login(self):
        response = self.client.post('/user/login', data=dict(
            email='test@naver.com',
            password='PASSWORD',
        ))

        self.assertEqual(response.status_code, 200)