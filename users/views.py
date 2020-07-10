from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username.capitalize()}')
            return redirect('messages_page')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup_page.html', {'form': form})


def info_messages(request):
    return render(request, 'users/message_page.html')
