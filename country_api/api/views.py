from django.shortcuts import render
from django.db.models import F, Q, Sum
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import permissions
from django_ratelimit.decorators import ratelimit
from rest_framework_simplejwt.tokens import RefreshToken
from ..core.models import CountryData
from ..core.serializers import CountrySerializer


def get_tokens_for_user(user):
    return str(RefreshToken.for_user(user).access_token)

class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    @method_decorator(ratelimit(key='post:request.data["username"]', rate="10/30m"))
    def post(self, request):
        is_too_many = getattr(request, 'limited', False)
        if is_too_many:
            return JsonResponse({'message':'Too Many Login Attempts. Please Try again Later','status':429}, status=429)
        
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        
        if len(username)==0 or len(password)==0:
            return JsonResponse({'message':'Please Provide Username and Password','status':400})
        
        the_user = auth.authenticate(username=username, password=password)
        
        if the_user is not None:
            return JsonResponse({'message':'Success','status':200, 'token':get_tokens_for_user(the_user)})
        
        return JsonResponse({'message':'Username of Password is incorrect','status':401}, status=401)
        

class CountryList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        countries = CountrySerializer(CountryData.objects.all().order_by("common_name"), many=True).data
        
        return JsonResponse({'countries':countries, 'message':'Sucess','status':200})
        
