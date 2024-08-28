from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from django.http import JsonResponse
from django.http.response import JsonResponse
from .models import SellCountData
from django.utils import timezone
from .forms import DateSearchForm


def showerp(request):
    return render(request, 'erp/main.html')


def update_sell_count(request):
    if request.method == "POST":
        sell_alcol_id = request.POST.get('sell_alcol_id')
        sell_date = request.POST.get('sell_date')

        # sell_date를 DateField로 변환
        try:
            sell_date = timezone.datetime.strptime(sell_date, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': '잘못된 날짜 형식입니다.'}, status=400)

        # SellCountData 객체 검색
        obj, created = SellCountData.objects.get_or_create(
            sell_alcol_id=sell_alcol_id,
            sell_date=sell_date,
            defaults={'sell_count': 1}
        )

        if not created:
            # 객체가 이미 존재하면 sell_count를 증가시킴
            obj.sell_count += 1
            obj.save()

        return JsonResponse({
            'sell_alcol_id': obj.sell_alcol_id,
            'sell_date': obj.sell_date,
            'sell_count': obj.sell_count,
            'created': created
        })

    return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)


def sell_statistics(request):
    selldata_json = []
    if request.method == "POST":
        selected_date = request.POST.get('selected_date')
        if selected_date:
            sellcountdata = SellCountData.objects.filter(sell_date=selected_date)
            print(sellcountdata)
            for selldata in sellcountdata:
                selldata_json.append(
                    {
                        'sell_alcol_id': selldata.sell_alcol_id,
                        'sell_alcol_name': selldata.sell_alcol_name,
                        'sell_date': selldata.sell_date,
                        'sell_count': selldata.sell_count
                    }
                )
            return JsonResponse(selldata_json, safe=False)
    return render(request, 'erp/erpsell.html')


