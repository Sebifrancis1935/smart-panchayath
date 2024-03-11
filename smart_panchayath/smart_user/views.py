from django.shortcuts import render

# Create your views here.
from .models import Panchayath_details
from django.shortcuts import render, redirect
from . forms import UserForm, LoginForm, P_loginForm


def User_Registration(request):
    if request.method == 'POST':
        frm = UserForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('User_Login')

        else:
            # If the form is not valid, handle the error or alert the user
            # For instance, you could pass the form with errors back to the template
            return render(request, 'user_registration.html', {'frm': frm})
    else:
        frm = UserForm()

    return render(request, 'user_registration.html', {'frm': frm})


def User_Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Implement your login logic here
            # For demonstration purposes, let's just print the email and redirect to home
            email = form.cleaned_data['mail']
            print("Login successful for email:", email)
            # Redirect to home page after successful login
            return redirect('Home')
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form})


def Panchayath_Login(request):
    if request.method == 'POST':
        form = P_loginForm(request.POST)
        if form.is_valid():
            # Implement your login logic here
            # For demonstration purposes, let's just print the email and redirect to home
            id = form.cleaned_data['p_id']
            print("Login successful for email:", id)
            # Redirect to home page after successful login
            return redirect('Home')
    else:
        form = P_loginForm()
    return render(request, 'panchayath_login.html', {'form': form})


def Muncipality_Login(request):
    if request.method == 'POST':
        form = P_loginForm(request.POST)
        if form.is_valid():
            # Implement your login logic here
            # For demonstration purposes, let's just print the email and redirect to home
            id = form.cleaned_data['p_id']
            print("Login successful for email:", id)
            # Redirect to home page after successful login
            return redirect('Home')
    else:
        form = P_loginForm()
    return render(request, 'muncipality_login.html', {'form': form})


def Corporation_Login(request):
    if request.method == 'POST':
        form = P_loginForm(request.POST)
        if form.is_valid():
            # Implement your login logic here
            # For demonstration purposes, let's just print the email and redirect to home
            id = form.cleaned_data['p_id']
            print("Login successful for email:", id)
            # Redirect to home page after successful login
            return redirect('Home')
    else:
        form = P_loginForm()
    return render(request, 'corporation_login.html', {'form': form})


def Index(request):
    return render(request, 'index.html')


def Panchayath_list(request):
    panchayath_details = Panchayath_details.objects.all()
    return render(request, 'panchayath_list.html', {'panchayath_details': panchayath_details})


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Features(request):
    return render(request, 'features.html')


def Services(request):
    return render(request, 'services.html')


def error(request):
    return render(request, 'error.html')


def category(request):
    return render(request, 'category.html')


def job_detail(request):
    return render(request, 'job-detail.html')


def job_list(request):
    return render(request, 'job-list.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def Home(request):
    return render(request, 'home.html')
