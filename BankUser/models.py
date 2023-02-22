from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)
from django.db import models
from django.urls import reverse
from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _



# Create your models here.

class Bank(models.Model):

    card_choices = (
        ("D", "Debit"),
        ("C", "Credit"),

    )
    
    card = models.CharField(max_length = 30, choices = card_choices, default = "D")
    
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 30)
    

    def __str__(self):
        return f'{self.name} Bank'

class Customer(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
  
    def __str__(self):
        return self.user.first_name 
    
    def __str__(self):
        return self.address
    
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


def get_expiry():
    return datetime.today() + timedelta(days=3650)


class customerAccount(models.Model):

    gender_choices = (
        ("M" , "Male"),
        ("F" , "Female"),
    )

    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 10, choices = gender_choices)

    cardtype = models.ForeignKey(Bank, on_delete = models.CASCADE, default = "D")

    account_number = models.PositiveIntegerField(
        unique = True,

        validators = [
            MinValueValidator(10000000),
            MaxValueValidator(99999999)
        ]
    )

    openDate = models.DateField(default=timezone.now)
    expiryDate = models.DateField(default = get_expiry)

    def __str__(self):
        return str(self.account_number)


class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(customerAccount, on_delete = models.CASCADE)


class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(customerAccount, on_delete = models.CASCADE)


