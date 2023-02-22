from django.shortcuts import render
from  django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import auth
from . import forms,models
from .forms import CustomerAccountForm,CustomerForm,CustomerSignUpForm,WithdrawForm,DepositForm
from datetime import datetime,timedelta,date


def indexView(request):
    return render(request, 'bank/home.html')

def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('customersignup')
    return render(request,'bank/customerclick.html')

def customersignup_view(request):
    form=forms.CustomerSignUpForm()
    if request.method=='POST':
        form=forms.CustomerSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)

            return HttpResponseRedirect('customerlogin')
    return render(request,'bank/customersignup.html',{'form':form})

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


def afterlogin_view(request):
    return render(request, 'bank/customerafterlogin.html')

    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    # return render(request,'bank/customerafterlogin.html')
    # if is_customer(request.user):

    #     return render(request,'customerafterlogin')

    # if user.groups.filter(name='CUSTOMER').exists():
    #     return redirect('bank/customerafterlogin.html')
    # else:
    #     return redirect('bank/customerafterlogin.html')
   

def registerbank_view(request):
    
    form=forms.BankForm()
    if request.method=='POST':
        
        form=forms.BankForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bank/registerbank.html')
    return render(request,'bank/registerbank.html',{'form':form})

def createaccount_view(request):
    
    form=forms.CustomerAccountForm()
    if request.method=='POST':
        
        form=forms.CustomerAccountForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bank/createaccount.html')
    return render(request,'bank/createaccount.html',{'form':form})

def createcustomer_view(request):
    
    form=forms.CustomerForm()
    if request.method=='POST':
        
        form=forms.CustomerForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bank/createcustomer.html')
    return render(request,'bank/createcustomer.html',{'form':form})


def withdraw_view(request):
    
    form=forms.WithdrawForm()
    if request.method=='POST':
        
        form=forms.WithdrawForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bank/withdraw.html')
    return render(request,'bank/withdraw.html',{'form':form})

def deposit_view(request):
    
    form=forms.DepositForm()
    if request.method=='POST':
        
        form=forms.DepositForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'bank/deposit.html')
    return render(request,'bank/deposit.html',{'form':form})



