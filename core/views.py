from django.shortcuts import render, redirect
from .models import Character
from .forms import CharacterForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('core')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created succesfully')
                return redirect('login')

        data = {}
        data['form'] = form
        return render(request, 'register.html', data)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('core')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('core')
            else:
                messages.info(request, 'Username or Password is incorrect')

        data = {}
        return render(request, 'login.html', data)


def logoutUser(request):
    logout(request)
    return redirect('core')


def core(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def inventory(request):
    data = {}
    data['characters'] = Character.objects.filter(user=request.user)
    return render(request, 'inventory.html', data)


@login_required(login_url='login')
def form(request):
    data = {}
    data['form'] = CharacterForm()
    return render(request, 'form.html', data)


@login_required(login_url='login')
def create(request):
    form = CharacterForm(request.POST or None)
    user = request.user

    if form.is_valid():
        character = form.save(commit=False)
        character.user = user
        character.save()
        return redirect('inventory')


@login_required(login_url='login')
def info(request, pk):
    data = {}
    data['character'] = Character.objects.get(pk=pk)
    return render(request, 'views.html', data)


@login_required(login_url='login')
def edit(request, pk):
    data = {}
    data['character'] = Character.objects.get(pk=pk)
    data['form'] = CharacterForm(instance=data['character'])
    return render(request, 'form.html', data)


@login_required(login_url='login')
def update(request, pk):
    data = {}
    data['character'] = Character.objects.get(pk=pk)
    form = CharacterForm(request.POST or None, instance=data['character'])

    if form.is_valid():
        form.save()
        return redirect('inventory')


@login_required(login_url='login')
def delete(request, pk):
    db = Character.objects.get(pk=pk)
    db.delete()
    return redirect('inventory')
