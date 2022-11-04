from . import views
from django.conf import settings
from django.conf.urls.static import serve,static
from django.urls import path
from assessment_admin.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout


urlpatterns = [
    path('', views.home,name='userhome'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('usersign_up',views.usersignup,name='usersignup'),
    path('userlogout',views.user_logout_view,name='userlogout'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('view_cart',views.usercart,name='view_cart'),
    path('add_frm_cart',views.add_from_cart,name='add_frm_cart'),
    path('rmv_frm_cart',views.remove_from_cart,name='rmv_frm_cart'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
