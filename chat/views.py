from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Chat, Room as r
from django.http import HttpResponse, Http404
from django.contrib import auth, messages
from django.contrib.auth.models import User

import logging
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

ud=User
def login(request):
    return render(request, 'register_redirect.html')


# def register_redirect(request):
#     u = ud()
#     u.name = request.POST['name']
#     u.username = request.POST['login']
#     u.address1 = request.POST['address1']
#     u.address2 = request.POST['address2']
#     u.gender = request.POST['gender']
#     u.city = request.POST['city']
#     u.state = request.POST['state']
#     u.pincode = request.POST['pincode']
#     u.email = request.POST['email']
#     u.dob = request.POST['dob']
#     u.contact = request.POST['contact']
#     u.password = request.POST['password']
#     u.save()
#     return render(request, 'register_redirect.html')


def register(request):
    context = {}
    if 'name' in request.POST:
        context = {
            'name': request.POST['name'],
            'username': request.POST['username'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'gender': request.POST['gender'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'pincode': request.POST['pincode'],
            'email': request.POST['email'],
            'dob': request.POST['dob'],
            'contact': request.POST['contact'],
            'password': request.POST['password']
        }
    return render(request, 'register.html', context)


def save(request):
    data = ud()
    if 'name' in request.POST:
        data.name = request.POST['name']
        data.username = request.POST['login']
        data.address1 = request.POST['address1']
        data.address2 = request.POST['address2']
        data.gender = request.POST['gender']
        data.city = request.POST['city']
        data.state = request.POST['state']
        data.pincode = request.POST['pincode']
        data.email = request.POST['email']
        data.dob = request.POST['dob']
        data.contact = request.POST['contact']
        data.password = request.POST['password']
        data.save()


def handle_exception(e):
    print(e)


def logout(request):
    file = "logout.html"
    if 'roomId' in request.session:
        del request.session['roomId']
        del request.session['roomName']
    if 'user' in request.session:
        del request.session['user']
        del request.session['id']
    else:
        file = "login.html"
    return render(request, file)


def after_login(request):
    print("after login triggered")

    context = {}
    file = 'after_login.html'
    username_from_form = ""
    password_from_form = ""
    user = request.user

    try:
        if "username" in request.POST and "password" in request.POST:
            username_from_form = request.POST['username']
            password_from_form = request.POST['password']
        user = request.user
    except Exception as e:
        handle_exception(e)

    if user:
        context = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'address1': user.email,
        }
        request.session['id'] = user.id
        request.session['user'] = user.username
        request.session['add1'] = user.email
    else:
        context = {
            'username': "Not Found."
        }
        file = "login.html"
    return render(request, file, context)


def check_user(request):
    return render(request, "check_user.html")


def navigation(request):
    return render(request, "navigation.html")


def hackers(request):
    return render(request, "hackers.html")

@login_required(login_url='/accounts/login')
def chat(request):
    print("chat triggered")

    obj_chat = Chat.objects.all()
    rooms = r.objects.all()
    chats = Chat.objects.all()

    context = {
        'data1': obj_chat,
        'rooms':rooms,
        'chats':chats
    }
    return render(request, 'chat_new.html', context)


def chat_sender(request):
    obj_chat = Chat()
    print('this is the message--->', request.GET['chat'])
    chat = request.session['user'] + '\n---------------------\n' + request.GET['chat']
    obj_chat.uid = request.session['id']
    obj_chat.chat = chat
    obj_chat.roomid = request.session['roomId']
    obj_chat.save()
    return JsonResponse({'response': True}, safe=False)


def fetch(request):
    print("fetch triggered")
    obj_chat = Chat.objects.filter(roomid=request.session['roomId'])

    context = {
        'data1': obj_chat
    }
    return render(request, "fetch_chat.html", context)


# ----------------------------- R & D -----------------------------

def check_login(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        login = request.POST["login"]
        user = None
        try:
            try:
                user = ud.objects.get(username=login)
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."
    return JsonResponse(response_data)


def test(request):
    return render(request, "test_user.html", {})


def room(request):
    rooms = r.objects.all()
    if "room" in request.POST:
        room = r()
        room.name = request.POST["room"]
        room.save()
        return render(request, "room.html", {"room": rooms})
    return render(request, "room.html", {"room": rooms})


def selectRoom(request):

    if request.method=="GET":
        request.session["roomName"] = request.GET['name']
        request.session["roomId"] = request.GET['id']

        return redirect('/chat')


    if "room" in request.POST:
        roomData = request.POST["room"].split(',')
        request.session["roomId"] = roomData[0]
        request.session["roomName"] = roomData[1]
        return redirect('/chat')
