from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event,Location,EventType
from chat.models import Room
# Create your views here.
def index(request):
    return render(request,'index.html')

def event(request):
    data = Event.objects.all()
    location = Location.objects.all()
    event_type= EventType.objects.all()
    events = {
        "events":data,
        "locations":location,
        "event_types":event_type
    }
    return render(request,'events.html',events)

def create_event(request):

    if request.method == "POST":
        event_type = request.POST.get('event_type')
        location = request.POST.get('location')
        description = request.POST.get('description')
        date = request.POST.get('date')
        event = Event.objects.create(EventTypeDescription=EventType.objects.get(id=event_type),EventLocation=Location.objects.get(id=location),EventDate=date,EventDescription = description)
        event.save()
        room = Room.objects.create(name=EventType.objects.get(id=event_type).EventType)
        room.save()
    return redirect("/events")

def join_chat(request):
    if "room" in request.GET:
        room = Room.objects.get(name=request.GET.get("room"))
        request.session["roomId"] = room.id
        request.session["roomName"] = room.name
        return redirect('/chat')

def search(request):
    query = request.GET.get('query')
    
