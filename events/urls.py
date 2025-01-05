
from django.urls import path
from .import views
app_name = "events"

urlpatterns = [
    path('',views.upcoming_events, name="upcoming"),
    path('<slug:slug>/',views.my_events, name="my-event"),
]
