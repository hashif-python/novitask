from . import views
from django.conf import settings
from django.conf.urls.static import serve,static
from django.urls import path
from assessment_admin.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.home,login_url='userlogin'),name='userhome'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('usersign_up',views.usersignup,name='usersignup'),
    path('userlogout',login_required(views.user_logout_view,login_url='userlogin'),name='userlogout'),
    path('add_to_cart',login_required(views.add_to_cart,login_url='userlogin'),name='add_to_cart'),
    path('view_cart',login_required(views.usercart,login_url='userlogin'),name='view_cart'),
    path('add_frm_cart',login_required(views.add_from_cart,login_url='userlogin'),name='add_frm_cart'),
    path('rmv_frm_cart',login_required(views.remove_from_cart,login_url='userlogin'),name='rmv_frm_cart'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
