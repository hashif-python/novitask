from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from assessment_admin.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as dj_login
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
	products = Products.objects.all()
	try:
		cartval=UserCart.objects.filter(customer=request.user)
		cartval=len(cartval)
	except:
		cartval=0
	context = {'products':products,'cartlen':cartval}
	return render(request, 'userhome.html', context)


def userlogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		print(password)
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = dj_login(request, user)
			messages.success(request, f' Welcome {username} !!')
			return redirect('userhome')
		else:
			messages.info(request, f'Account Does Not Exit!!!, Try Again')

	return render(request,'userlogin.html')


def usersignup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('pass1')
		password2 = request.POST.get('pass2')

		if password1 == password2:
			password=make_password(password1)
			ob=User.objects.create(username=username,email=email,password=password)
			
			messages.success(request, f' Hi {username} !!, Your Account Has Been Created Successfully, Please Login')

			return redirect('userlogin')
		else:
			messages.danger(request, f'Something Went Wrong')


	return render(request,'userregister.html')


@login_required
def user_logout_view(request):
    logout(request)
    return redirect('userlogin')

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        item_code=request.POST.get('item_id')
        
        
        ob=Products.objects.get(id=item_code)
        try:
        	ob2= UserCart.objects.get(customer=request.user,product=ob)
        	ob2.quantity = int(ob2.quantity) + 1
        	ob2.total=int(ob2.total) + int(ob.amount)
        	ob2.save()
        	print(item_code)
        except:
        	ob2= UserCart.objects.create(customer=request.user,product=ob,quantity=1,amount=ob.amount,total=ob.amount)

        cartval=UserCart.objects.filter(customer=request.user)
        
        return JsonResponse({'message':'success','cartval':len(cartval)})

@login_required
def usercart(request):
	cartval=UserCart.objects.filter(customer=request.user)
	gtot=0
	for i in cartval:
		gtot+=int(i.total)
	context={
	'ob':UserCart.objects.filter(customer=request.user),
	'cartlen':len(cartval),
	'gtot':gtot
	}
	return render(request,'usercart.html',context)

@login_required
def add_from_cart(request):
    if request.method == 'POST':
        item_code=request.POST.get('item_id')
        
        
        ob=Products.objects.get(id=item_code)
        try:
        	ob2= UserCart.objects.get(customer=request.user,product=ob)
        	ob2.quantity = int(ob2.quantity) + 1
        	ob2.total=int(ob2.total) + int(ob.amount)
        	ob2.save()
        	print(item_code)
        except:
        	ob2= UserCart.objects.create(customer=request.user,product=ob,quantity=1,amount=ob.amount,total=ob.amount)

        ob3= UserCart.objects.filter(customer=request.user)
        gtot=0
        for i in ob3:
        	gtot+=int(i.total)

        cartval=UserCart.objects.filter(customer=request.user)
        
        return JsonResponse({'message':'success','cartval':len(cartval),'total':ob2.total,'qty':ob2.quantity,'gtot':gtot})

@login_required
def remove_from_cart(request):
	if request.method == 'POST':
		item_code=request.POST.get('item_id')


		ob=Products.objects.get(id=item_code)
        
		ob2= UserCart.objects.get(customer=request.user,product=ob)
		qty=int(ob2.quantity)
		if int(ob2.quantity) == 1:
			print('Hi2')
			ob2.delete()

		else:
			print('Hi2')
			ob2.quantity = int(ob2.quantity) - 1
			ob2.total=int(ob2.total) - int(ob.amount)
			ob2.save()
			print(item_code)

		try:
			ob3= UserCart.objects.filter(customer=request.user)
			gtot=0
			for i in ob3:
				gtot+=int(i.total)
		except:
			gtot=0

		cartval=UserCart.objects.filter(customer=request.user)
		if qty == 1:
			return JsonResponse({'message':'item_deleted','cartval':len(cartval),'gtot':gtot})
		else:
			return JsonResponse({'message':'success','cartval':len(cartval),'total':ob2.total,'qty':ob2.quantity,'gtot':gtot})