from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import serve,static


urlpatterns = [
    path('',views.adminlogin,name='adminlogin'),
    path('admin-logout-view',views.admin_logout_view,name='admin_logout_view'),
    path('admin_dashboard',login_required(views.adminhome,login_url='adminlogin'),name='adminhome'),
    path('view_product',login_required(views.view_products, login_url='adminlogin'),name='view_products'),
    path('add_product',login_required(views.add_products, login_url='adminlogin'),name='add_products'),
    path('edit_product/<int:id>',login_required(views.edit_products, login_url='adminlogin'),name='edit_product'),
    path('delete_product/<int:id>',login_required(views.delete_products, login_url='adminlogin'),name='delete_product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
