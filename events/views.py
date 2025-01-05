from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from.models import myevent
from .import forms
# Create your views here.

def upcoming_events(request):
    myevents = myevent.objects.all().order_by("-date")
    return render(request, 'events/upcoming_events.html', {'myevents':myevents})


def my_events(request, slug):
    theevent = myevent.objects.get(slug=slug)
    return render(request, 'events/my_events.html',{'theevent':theevent})



@login_required(login_url="/users/login/")
def create_events(request):
    if request.method == "POST":
        form = forms.CreateEvent(request.POST, request.FILES)
        if form.is_valid():
            newevent = form.save(commit=False)
            newevent.author = request.user
            newevent.save()
            return redirect('events:upcoming')
    
    else:
        form = forms.CreateEvent()
    return render(request, 'events/create_event.html', {'form':form})