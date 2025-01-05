from django.shortcuts import render

from.models import myevent

# Create your views here.

def upcoming_events(request):
    myevents = myevent.objects.all().order_by("-date")
    return render(request, 'events/upcoming_events.html', {'myevents':myevents})


def my_events(request, slug):
    theevent = myevent.objects.get(slug=slug)
    return render(request, 'events/my_events.html',{'theevent':theevent})