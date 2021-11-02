from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import LogInForm, SignUpForm, PostForm
from .forms import User, Post

def home(request):
    return render(request, 'home.html')

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credential provided are invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def feed(request):
    queryset = Post.objects.all()
    context = {"object_list" : queryset}
    return render(request, 'feed.html', context)

def new_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            post=Post(author=current_user)
            form=PostForm(request.POST, instance=post)
            form.save()
            return redirect('feed')
    form = PostForm()
    return render(request, 'new_post.html', {'form' : form})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('home')

def user_list(request):
    queryset = User.objects.all()
    context = {"object_list" : queryset}
    return render(request, 'user_list.html', context)

def show_user(request, user_id):
    person = User.objects.all().get(id=user_id)
    posts = Post.objects.all().filter(author=person)
    return render(request, 'show_user.html', {'user': person, 'object_list': posts})
