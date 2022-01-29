from django.shortcuts import render
from django.http import JsonResponse
from recharge.models import Operator,Recharge, Plan
from django.views.decorators.csrf import csrf_exempt
import traceback
# Create your views here.

def index(request):
    if request.method == 'GET':
        operators = Operator.objects.all()
        return render(request,'index.html',{'operator':operators})
    
@csrf_exempt
def getPlans(request,provider:str):
    try:
        allPlans = Plan.objects.filter(operator=provider)
        if allPlans.count() == 0:
            return JsonResponse({'status':'error','message':'No Plans Found'})
    except:
        return JsonResponse({'status':'error','message':'No Plans Found'})
    final = {}
    for o in allPlans:
        final[o.id]={
                'name':o.name,
                'price':o.price,
                'details':o.detail,
                'internet':o.internet,
                'call':o.call,
                'sms':o.sms,
                'validity':o.validity
        }
    return JsonResponse({
        'status':'success',
        'message':str(allPlans.count())+' Plans Found',
        'plans':final
    })
        
  
@csrf_exempt  
def getOperators(request):
    try:
        temp = Operator.objects.all()

        return JsonResponse({'status':'success','data':temp})
    except:
        return JsonResponse({'status':'failure','data':[]})

def raiseError():
    raise ValueError('No Data')

@csrf_exempt
def doRecharge(request):
    if request.method == 'POST':
        # return JsonResponse(request.POST)
        finalSet = {}
        try:
            finalSet['number'] = request.POST.get('number')
            if finalSet['number'] is None: raise ValueError('No Number Provided')
            finalSet['operator'] = Operator.objects.get(id=int(request.POST.get('operator')))
            finalSet['plan'] = finalSet['operator'].plan_set.get(id=int(request.POST.get('plan')))        
        except:
            traceback.print_exc()
            return JsonResponse({'status':'failure','message':'Invalid Request'})
        finalSet['success'] = True
        try:
            rech = Recharge.objects.create(**finalSet)
        except:
            traceback.print_exc()
            return JsonResponse({'status':'failure','message':'Something went Wrong'})
        return JsonResponse({'status':'success','message':'Recharge Successful','referenceID':rech.id})                    