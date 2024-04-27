
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def hello1(request):
    return HttpResponse("<center>Welcome to SPA Homepage</center>")
def projecthome(request):
    return render(request,'projecthome.html')
def signup(request):
    return render(request,'signup.html')
from django.contrib.auth.models import User,auth
from django.contrib import messages
def signup1(request):
    if request.method == 'POST':
        username= request.POST['username']
        pass1= request.POST['password']
        pass2= request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'signup.html')
            else:
                user=User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!')
                return render(request,'projecthome.html')
        else:
            messages.info(request, 'Password does not match.')
            return render(request, 'signup.html')

def login(request):
    return render(request,'login.html')
def login1(request):
    if request.method =='POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not  None:
            auth.login(request, user)
            if len(username)==10:
                return redirect('myhome')
            elif len(username)==4:
                return redirect('sellerhome')
            else:
                return redirect('projecthome')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'projecthome.html')





def myhome(request):
    return render(request,'myhome.html')
def feedback(request):
    return render(request,'feedback.html')
from .models import Feedback


from django.shortcuts import render
from .models import Feedback

def feedback1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        feedback1 = Feedback.objects.create(name=name, email=email, rating=rating, comment=comment)
        feedback1.save()
        return render(request, 'thank_you.html')

    return render(request, 'feedback.html')


def thank_you(request):
    return render(request, 'thank_you.html')
def sellerhome(request):
    return render(request,'sellerhome.html')
def mydeals(request):
    return render(request,'todaysdeal.html')
def addproducts(request):
    return render(request,'addproducts.html')
def add_details(request):
    if request.method == 'POST':
        product_name = request.POST.get('productname')
        product_price = request.POST.get('price')
        categories = request.POST.get('productcatg')
        description = request.POST.get('productdesc')
        product_image = request.FILES.get('productimage')

        product_details=ProductDetails(
            product_name=product_name,
            product_price=product_price,
            categories= categories,
            description=description,
            product_image=product_image,
        )
        product_details.save()
        return render(request,'datainserted.html')
    return render(request, 'sellerhome.html')
def view_seller_products(request):
    if request.method == 'GET':
        product_details_list = ProductDetails.objects.all()
        return render(request, 'view_seller_products.html', {'product_details_list': product_details_list})



from django.shortcuts import render
from .models import ProductDetails  # Import the ProductDetails model

def viewproducts(request):
    if request.method == 'GET':
        product_details_list = ProductDetails.objects.all()
        return render(request, 'viewproducts.html', {'product_details_list': product_details_list})

def skincare(request):
    return render(request,'skincare.html')
def makeup(request):
    return render(request,'makeup.html')
def fragrance(request):
    return render(request,'fragrance.html')
def buynow(request):
    return render(request,'buynow.html')

def cart(request):
    return render(request,'cart.html')
