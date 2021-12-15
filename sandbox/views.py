from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.defaulttags import register

from sandbox.forms import UserForm, MessageForm
from sandbox.models import Message


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def message_list(request):
    return render(request, 'sandbox/base.html', {})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return redirect('create_user')
    else:
        form = UserForm()

    return render(request, 'sandbox/create_user.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        kwargs = {}
        if username := request.POST.get('username'):
            kwargs['username'] = username
        if email := request.POST.get('email'):
            kwargs['email'] = email
        if password := request.POST.get('password'):
            kwargs['password'] = password

        user = authenticate(request, **kwargs)
        if user is not None:
            login(request, user)
            return redirect('index')

    else:
        return render(request, 'sandbox/log_in.html', {})


def index(request):
    if request.method == "POST":
        for filename, file in request.FILES.items():
            print(request.FILES[filename].name)
        print(request.POST)
    return render(request, 'sandbox/index.html', {})


def chat(request, username=None):
    messages = [
        {
            'user': 'other',
            'text': 'Привет, Николай!',
            'image': 'https://media.istockphoto.com/photos/prize-wheel-picture-id175482570'
        },
        {
            'user': 'current',
            'text': 'Руслан, добрый день!',
            'image': "https://media.istockphoto.com/photos/prize-wheel-picture-id175482570"
        },
        {
            'user': 'current',
            'text': 'Еще одно сообщение, без изображения'
        }
    ]
    if username is None:
        print("Main chat page")
    else:
        # print(f"request.user.username = {request.user.username}")
        # print(f"username = {username}")
        # print("all messages")
        # for message in Message.objects.filter():
        #     print(f"author: {message.author.username}")
        #     print(message)
        filtered_messages = Message.objects.filter(
            Q(author__username=request.user.username) & Q(recipient__username=username) |
            Q(author__username=username) & Q(recipient__username=request.user.username)).order_by('created_date')
        for message in filtered_messages:
            res = {}
            # if message.image is not None:
            #     with open (message.image)
        messages = [
            {
                'author': message.author.username,
                'text': message.text
            } |
            ({
                'image': message.image
            } if message.image is not None else {})
            for message in filtered_messages
        ]

    # if username is None:
    #     pass
    # else:
    #     for mess in User.objects.filter():
    #         pass
    return render(request, 'sandbox/chat.html', {'messages': messages, 'username': username})


def create_message(request):
    if request.method == "POST":
        args = request.POST.copy()
        args['recipient'] = User.objects.get(username=request.POST['recipient']).pk
        args['author'] = request.user.pk
        print(args)
        for filename, file in request.FILES.items():
            print(request.FILES[filename].name)
        form = MessageForm(args)
        if form.is_valid():

            new_message = Message.objects.create(**form.cleaned_data, files=request.FILES)
            return redirect('chat')
