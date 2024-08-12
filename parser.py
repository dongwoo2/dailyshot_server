import json

import sys,io,os
import django

sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stdout=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from map.models import Alcolshop # 정보를 저장할 장고의 모델을 불러오기

def parsing():

    with open('package.json') as json_file: # json 파일을 열고, 그 안의 데이터를 불러옵니다.
        json_data = json.load(json_file)

    post = []

    for i in range(2):
        post.append({
            'name': json_data['alcolshops'][i]['name'],
            'loc': json_data['alcolshops'][i]['loc'],
            'lat': json_data['alcolshops'][i]['lat'],
            'lon': json_data['alcolshops'][i]['lon'],
        })

        return post

    if __name__ == '__main__':
        post = parsing()

        for i in range(len(post)):
            Alcolshop(
                name=post[i]['name'],
                location=post[i]['loc'],
                latitude=post[i]['lat'],
                longitude=post[i]['lon'],
            ).save()
