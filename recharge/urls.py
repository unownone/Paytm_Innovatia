from django.urls import path
from recharge import views

app_name = 'recharge'

urlpatterns = [
    path('', views.index, name='index'),
    path('recharge/',views.doRecharge, name='recharge'),
    path('getPlans/<str:provider>', views.getPlans, name='getPlans'),
    path('getOperators/', views.getOperators, name='getOperators'),
]
