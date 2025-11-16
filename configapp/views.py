from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# ✅ BOSH SAHIFA - BU FUNKSIYA MAVBUD BO'LISHI KERAK
def home(request):
    return render(request, 'index.html')


# ✅ LOGIN
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Xush kelibsiz, {user.username}!')
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')

    return render(request, 'login.html')


# ✅ LOGOUT
def custom_logout(request):
    logout(request)
    messages.success(request, 'Siz tizimdan muvaffaqiyatli chiqdingiz!')
    return redirect('home')


# ✅ RO'YXATDAN O'TISH
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ro‘yxatdan muvaffaqiyatli o‘tdingiz!')
            return redirect('user_dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


# ✅ ADMIN DASHBOARD
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sizga bu sahifaga kirish ruxsati yo‘q!')
        return redirect('user_dashboard')
    return render(request, 'admin_dashboard.html')


# ✅ USER DASHBOARD
@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')


# ✅ BOG'LANISH
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Bu yerda email yoki ma'lumotlar bazasiga saqlash logikasi
        messages.success(request, f'Rahmat, {name}! Xabaringiz qabul qilindi. Tez orada siz bilan bog\'lanamiz.')
        return redirect('contact')

    return render(request, 'contact.html')


# ✅ BIZ HAQIMIZDA
def about(request):
    return render(request, 'about.html')


# ✅ LOYIHALAR
def design(request):
    return render(request, 'design.html')


# ✅ KOMPANIYA
def company(request):
    return render(request, 'company.html')


# ✅ YANGILIKLAR
def news(request):
    return render(request, 'news.html')