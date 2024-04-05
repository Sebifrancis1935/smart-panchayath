from .models import Panchayath_details, Muncipality_details
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserForm, LoginForm, PanchayathLoginForm, MuncipalityLoginForm, CorporationLoginForm
from .models import User, Panchayath, Muncipality, Corporation


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
            email = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(mail=email, password=password)
                return redirect('Home')
            except User.DoesNotExist:
                return render(request, 'user_login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form})


def panchayath_login(request):
    if request.method == 'POST':
        form = PanchayathLoginForm(request.POST)
        if form.is_valid():
            p_id = form.cleaned_data['p_id']
            password = form.cleaned_data['password']
            try:
                panchayath_user = Panchayath.objects.get(p_id=p_id)
                if panchayath_user.password == password:
                    # Add logic for successful login
                    messages.success(request, 'Login successful!')
                    # Replace 'home' with your desired redirect URL
                    return render(request, 'home.html')
                else:
                    messages.error(
                        request, 'Invalid credentials. Please try again.')
            except Panchayath.DoesNotExist:
                messages.error(
                    request, 'Invalid credentials. Please try again.')
    else:
        form = PanchayathLoginForm()
    return render(request, 'panchayath_login.html', {'form': form})


def muncipality_login(request):
    if request.method == 'POST':
        form = MuncipalityLoginForm(request.POST)
        if form.is_valid():
            m_id = form.cleaned_data['m_id']
            password = form.cleaned_data['password']
            try:
                muncipality_user = Muncipality.objects.get(m_id=m_id)
                if muncipality_user.password == password:
                    # Add logic for successful login
                    messages.success(request, 'Login successful!')
                    # Replace 'home' with your desired redirect URL
                    return redirect('home')
                else:
                    messages.error(
                        request, 'Invalid credentials. Please try again.')
            except Muncipality.DoesNotExist:
                messages.error(
                    request, 'Invalid credentials. Please try again.')
    else:
        form = MuncipalityLoginForm()
    return render(request, 'muncipality_login.html', {'form': form})


def corporation_login(request):
    if request.method == 'POST':
        form = CorporationLoginForm(request.POST)
        if form.is_valid():
            c_id = form.cleaned_data['c_id']
            password = form.cleaned_data['password']
            try:
                corporation_user = Corporation.objects.get(c_id=c_id)
                if corporation_user.password == password:
                    # Add logic for successful login
                    messages.success(request, 'Login successful!')
                    # Replace 'home' with your desired redirect URL
                    return redirect('home')
                else:
                    messages.error(
                        request, 'Invalid credentials. Please try again.')
            except Corporation.DoesNotExist:
                messages.error(
                    request, 'Invalid credentials. Please try again.')
    else:
        form = CorporationLoginForm()
    return render(request, 'corporation_login.html', {'form': form})


def Index(request):
    return render(request, 'index.html')


def Panchayath_list(request):
    panchayath_details = Panchayath_details.objects.all()
    return render(request, 'panchayath_list.html', {'panchayath_details': panchayath_details})


def Muncipality_list(request):
    muncipality_details = Muncipality_details.objects.all()
    return render(request, 'muncipality_list.html', {'muncipality_details': muncipality_details})


def about_us(request):
    return render(request, 'index_about.html')


def contact_us(request):
    return render(request, 'index_contact.html')


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
