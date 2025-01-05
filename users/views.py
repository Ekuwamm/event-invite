from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.



def register_views(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('events:upcoming')
        
    else:
        form = UserCreationForm()
    return render(request, 'users/register_views.html', {'form':form})


def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
          login(request, form.get_user())
          if "next" in request.POST:
              return redirect(request.POST.get("next")) 
          else:
              return redirect('events:upcoming')
        
    else:
       form = AuthenticationForm()
    return render(request, 'users/login_views.html', {'form':form})


def logout_views(request):
    if request.method == "POST":
        logout(request)
        return redirect('events:upcoming')
    return render(request, 'users/logout_views.html')