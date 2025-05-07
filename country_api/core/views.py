from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import JsonResponse
from .utils.decorators import login_required
from .models import CountryData


def is_ajax(request):
    return (request.headers.get('x-requested-with') == 'XMLHttpRequest')

@login_required
def index(request):
    context = {
        "countries":CountryData.objects.all().order_by("common_name"),
    }
    return render(request, "core/index.html", context)

def login(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    if is_ajax(request) and request.method=="POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        if len(username)==0 or len(password)==0:
            return JsonResponse({"status":400})
        
        the_user = auth.authenticate(username=username, password=password)
        if the_user is not None:
            auth.login(request, the_user)
            return JsonResponse({"status":200})
        return JsonResponse({"status":401})
        
    return render(request, "core/login.html")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('core:login')
