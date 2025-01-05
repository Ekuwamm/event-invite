
from django.urls import path
from .import views
app_name = "events"

urlpatterns = [
    path('',views.upcoming_events, name="upcoming"),
    path('new-event/', views.create_events, name="new-event"),
    path('<slug:slug>/',views.my_events, name="my-event"),
]
