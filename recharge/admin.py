from django.contrib import admin
from recharge.models import Operator,Plan,Recharge
# Register your models here.




admin.site.register(Operator)
admin.site.register(Plan)
admin.site.register(Recharge)