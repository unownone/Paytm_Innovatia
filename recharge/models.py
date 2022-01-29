from django.db import models

# Create your models here.
    
class Operator(models.Model):
    """Stores All Operators
    """
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Plan(models.Model):
    """Stores All Plans
        prepaid: Checks whether is prepaid or postpaid [true for prepaid, false for postpaid]
        name : Name of the plan if any
        price : price of the plan
        detail : general Description of the plan
        Internet : Amount of internet data available
        Call : Whether call minutes available or not
        SMS : Amount of SMS available
        Validity : Days worth of validity
    """
    prepaid = models.BooleanField(default=True)
    name = models.CharField(max_length=10,null=True,blank=True)
    price = models.IntegerField()
    detail = models.CharField(max_length=200,null=True,blank=True)
    internet = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    call = models.BooleanField(default=False)
    sms = models.IntegerField(null=True,blank=True)
    validity = models.IntegerField(null=True,blank=True)
    operator = models.ForeignKey(Operator,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.price) + '' + str(self.name if self.name is not None else '')

class Recharge(models.Model):
    """
        STORES all the recharges as models.
    """
    success = models.BooleanField(default=False)
    number = models.CharField(max_length=12)
    username = models.CharField(max_length=50, null=True, blank=True)
    operator = models.ForeignKey(Operator, related_name='operator', on_delete=models.CASCADE,null=True,blank=True)
    plan = models.ForeignKey(Plan, related_name='plan', on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(null=True, blank=True,auto_now=True)
        
    def __str__(self):
        return self.number + ' of Rs '+ str(self.plan.price)
    
