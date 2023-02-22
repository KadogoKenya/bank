from django import forms
from django.db import models
from django import forms 
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.contrib.auth.forms import UserCreationForm
from BankUser.models import Customer,Withdraw,Deposit,customerAccount,Bank

class CustomerSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name','card','location']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']

class CustomerAccountForm(forms.ModelForm):
    class Meta:
        model = customerAccount
        fields = ['customer','cardtype','gender','account_number','openDate','expiryDate']

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdraw
        fields = ['amount','account']


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount','account']

