from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Service, ServiceCategory, Master, Appointment, Review
from .forms import AppointmentForm, ReviewForm


# 1. Главная
def home(request):
    popular = Service.objects.filter(is_active=True).order_by('price')[:6]
    return render(request, 'home.html', {'popular_services': popular})


# 2. Услуги
def services(request):
    categories = ServiceCategory.objects.prefetch_related('services').all()
    return render(request, 'services.html', {'categories': categories})


# 3. Мастера
def masters(request):
    masters_qs = Master.objects.filter(is_active=True)
    return render(request, 'masters.html', {'masters': masters_qs})


# 4. Запись (форма)
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка принята! Мы свяжемся с вами.")
            return redirect('appointment')
    else:
        initial_data = {}
        if request.GET.get('service'):
            initial_data['service'] = request.GET.get('service')
        form = AppointmentForm(initial=initial_data)

    return render(request, 'appointment.html', {'form': form})


# 5. Контакты (ИМЕННО ЭТОЙ ФУНКЦИИ НЕ ХВАТАЕТ!)
def contacts(request):
    return render(request, 'contacts.html')


# 6. Регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Аккаунт создан! Теперь вы можете войти.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# 7. Личный кабинет
@login_required
def profile(request):
    user_appointments = Appointment.objects.filter(name=request.user.username)
    reviews = Review.objects.all()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, "Спасибо за отзыв!")
            return redirect('profile')
    else:
        review_form = ReviewForm()

    context = {
        'appointments': user_appointments,
        'reviews': reviews,
        'review_form': review_form
    }
    return render(request, 'profile.html', context)