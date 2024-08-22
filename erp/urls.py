from django.urls import path
from .views import update_sell_count, sell_statistics, showerp


app_name = 'erp'

urlpatterns = [
    path('showerp', showerp, name='showerp'),
    path('update_sellcount/', update_sell_count, name='update_sellcount'),
    path('sell_statistics/', sell_statistics, name='sell_statistics'),
]
