from . import views 
from django.urls import path,include
# from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static



urlpatterns = [
    path('home', views.indexView, name='index'),
    path('customerclick', views.customerclick_view),
    path('customersignup', views.customersignup_view),
    path('customerlogin', LoginView.as_view(template_name='bank/customerlogin.html')),
    # path('afterlogin',views.afterlogin_view, name = 'afterlogin_view'),
    path('',views.afterlogin_view, name = 'afterlogin'),
    

    path('registerbank', views.registerbank_view),
    path('createaccount', views.createaccount_view),
    path('createcustomer', views.createcustomer_view),
    path('withdraw', views.withdraw_view),
    path('deposit', views.deposit_view),
    


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)