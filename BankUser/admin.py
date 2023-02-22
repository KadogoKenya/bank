from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bank,Customer,customerAccount,Withdraw,Deposit
# Register your models here.
class BankAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bank, BankAdmin)


class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)


class customerAccountAdmin(admin.ModelAdmin):
    pass
admin.site.register(customerAccount, customerAccountAdmin)

class WithdrawAdmin(admin.ModelAdmin):
    pass
admin.site.register(Withdraw, WithdrawAdmin)


class DepositAdmin(admin.ModelAdmin):
    pass
admin.site.register(Deposit, DepositAdmin)
