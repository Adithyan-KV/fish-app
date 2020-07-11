from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username.capitalize()}!,'
                ' your account has been created.'
                ' Go to the Login page to access your account')
            return redirect('home_page')
        # else:
        #     error_list = form.error_messages
        #     for error in error_list:
        #         messages.error(request, f'Sorry {error_list} error happened')
    else:
        form = SignUpForm()
    return render(request, 'users/signup_page.html', {'form': form})
