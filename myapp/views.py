from django.shortcuts import render, redirect, HttpResponse
from .models import Caretaker, Careseeker
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .custom_get_user_model import get_user_model2


# Create your views here.
def home(request):
    return render(request, 'home.html')


def all_careseekers(request):
    if request.user.is_authenticated:
        all_users = Careseeker.objects.all()
        return render(request, 'all_careseekers.html', {'all_users': all_users})
    else:
        return HttpResponse('User is not authenticated')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user._meta.db_table == 'myapp_caretaker':
                login(request, user)
                return redirect('all_careseekers')
            else:
                login(request, user)
                return HttpResponse('here we will display all caretakers')

        else:
            messages.info(request, "password or email is incorrect")
            return redirect('login_view')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def caretaker_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        experience = request.POST.get('experience')
        ID_card = request.POST.get('ID_card')
        profession = request.POST.get('profession')
        objective = request.POST.get('objective')
        image = request.FILES.get('image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                messages.info(request, "Your email already exists. Please log in.")
                return redirect('caretaker_register')
            else:
                caretaker = User(
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    gender=gender,
                    age=age,
                    phone=phone,
                    experience=experience,
                    id_card_number=ID_card,
                    profession=profession,
                    objective=objective,
                    image=image,
                    password=make_password(password1)
                )
                caretaker.save()
                messages.info(request, "Congratulations! You are already registered!")
                return redirect('login_view')

        messages.info(request, "Please check your password confirmation!")

    return render(request, 'caretaker_register.html')


def careseeker_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        order = request.POST.get('order')
        image = request.FILES.get('image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            User = get_user_model2()
            if User.objects.filter(email=email).exists():
                messages.info(request, "Your email already exists. Please log in.")
                return redirect('careseeker_register')
            else:
                careseeker = User(
                    firstname=firstname, lastname=lastname,
                    age=age, gender=gender, email=email,
                    phone=phone, state=state, city=city,
                    address=address, order=order, image=image,
                    password=make_password(password1)
                )
                careseeker.save()
                messages.info(request, "Congratulations! You are already registered!")
                return redirect('login_view')

    return render(request, 'careseeker_register.html')


def user_profile(request):
    return render(request, 'user_data.html')




"""        if Caretaker.objects.get(email=email, password=password):
            user = Caretaker.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            all_users = Caretaker.objects.all()
            return render(request, 'all_careseekers.html', {'all_users': all_users})
        elif Careseeker.objects.get(email=email, password=password):
            user = Careseeker.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            return redirect('all_caretakers')

        messages.info("password or email is incorrect")
"""
