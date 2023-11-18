from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def index(request):
    obj = Article.objects.all()
    return render(request, 'index.html', {'result': obj})

# def register(request):
#     if request.method == 'POST':
#         # ... (your registration logic remains the same)
#         return redirect('/login/')
#     return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/new-page/')
        else:
            messages.info(request, "Invalid login")
            return redirect('/login/')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# def new_page(request):
#     # Your logic for the new_page view goes here
#     return render(request, 'new_page.html')
# def new_page(request):
#     if request.method == 'POST':
#         # Get form data
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone_number = request.POST.get('phone_number')
#         mail_id = request.POST.get('mail_id')
#         address = request.POST.get('address')
#         department = request.POST.get('department')
#         purpose = request.POST.get('purpose')
#         materials_provide = request.POST.getlist('materials_provide')
#
#         # Process the form data (you might want to save it to the database or perform some actions)
#
#         # For simplicity, rendering the same page after form submission
#         return render(request, 'new_page.html')
#
#     return render(request, 'new_page.html')
# def new_page(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         department = request.POST.get('department')
#         course = request.POST.get('course')
#         purpose = request.POST.get('purpose')
#         materials_provide = request.POST.getlist('materials')
#
#         # Process the form data as needed
#         # Here, you can perform database operations or any other actions with the form data
#
#         return HttpResponse("Form submitted successfully!")  # Modify this as needed
#
#     return render(request, 'new_page.html')


def new_page(request):
    if request.method == 'POST':
        # Fetch form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials_provide = request.POST.getlist('materials')

        # Set the confirmation message
        order_confirmed = "Order Confirmed"  # You can set this message as per your requirements

        return render(request, 'new_page.html', {'order_confirmed': order_confirmed})

    return render(request, 'new_page.html')


def register(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword :
            if User.objects.filter(username=username).exists() :
                messages.info(request, "Username already taken")
                return redirect('/register/')
            elif User.objects.filter(email=email).exists() :
                messages.info(request, "Email already taken")
                return redirect('/register/')
            else :
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                email=email, last_name=last_name)
                user.save()
                return redirect('/login/')
        else :
            messages.info(request, "Passwords not matching")
            return redirect('/register/')

    return render(request, "register.html")

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')