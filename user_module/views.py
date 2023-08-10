import time

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import login, logout
from utils.email_service import send_email
from user_module.forms import RegisterForm, loginForm, ForgotPasswordForm, ResetPasswordForm
from django.contrib import messages



class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'user_module/signup.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user_name = register_form.cleaned_data.get('username')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            name = register_form.cleaned_data.get('name')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    first_name=name,
                    email=user_email,
                    email_active_code=get_random_string(length=72),
                    is_active=False,
                    username=user_name,)
                new_user.set_password(user_password)
                # new_user.save()
                # send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'email/activate_account.html')
                # messages.success(request, 'ایمیل فعال سازی حساب کاربری یرای شما ارسال شد')
                return JsonResponse({
                    'status': 'tt'})
                time.sleep(5)
                return redirect(reverse('register_page'))
        else:
            print('noo')

        context = {
            'register_form': register_form
        }

        return render(request, 'user_module/signup.html', context)





class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user= User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('logi_page'))
            else:
                # todo: show your account was activated message to user
                print('npooo')

        return redirect(reverse('login_page'))




class LoginView(View):
    def get(self, request):
        logi_form = loginForm()
        context = {
            'logi_form': logi_form
        }

        return render(request, 'user_module/login.html', context)

    def post(self, request: HttpRequest):
        logi_form = loginForm(request.POST)
        if logi_form.is_valid():
            user_email = logi_form.cleaned_data.get('email')
            user_pass = logi_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    logi_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        logi_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                logi_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'logi_form': logi_form
        }

        return render(request, 'user_module/login.html', context)


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'user_module/forget_pass.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user:
                # send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot_password.html')
                messages.success(request,'sent')
                return redirect(reverse('home_page'))
            else:
                messages.error(request,'not user')

        context = {'forget_pass_form': forget_pass_form}
        return render(request, 'user_module/forget_pass.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('logi_page'))

        reset_pass_form = ResetPasswordForm()

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'user_module/reset-pass.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('logi_page'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'user_module/reset-pass.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
