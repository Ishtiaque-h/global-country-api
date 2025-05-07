from django.shortcuts import render
from django.db.models import F, Q, Sum
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework import permissions
from django_ratelimit.decorators import ratelimit
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiParameter
from ..core.models import CountryData
from ..core.serializers import CountrySerializer, LoginSerializer


def get_tokens_for_user(user):
    return str(RefreshToken.for_user(user).access_token)

class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    
    @extend_schema(request=LoginSerializer)
    @method_decorator(ratelimit(key='post:request.data["username"]', rate="10/30m"))
    def post(self, request):
        is_too_many = getattr(request, 'limited', False)
        if is_too_many:
            return JsonResponse({'message':'Too Many Login Attempts. Please Try again Later','status':429}, status=429)
        
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            the_user = auth.authenticate(username=serializer.validated_data["username"], password=serializer.validated_data["password"])
            if the_user is not None:
                return JsonResponse({'message':'Success','status':200, 'token':get_tokens_for_user(the_user)})
            return JsonResponse({'message':'Username of Password is incorrect','status':401}, status=401)
        
        return JsonResponse({'message':'Please provide usernamd and password','status':400})
        

class CountryList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        countries = CountrySerializer(CountryData.objects.all().order_by("common_name"), many=True, exclude_fields=True).data
        
        return JsonResponse({'countries':countries, 'message':'Sucess','status':200})
        

class CountryDetails(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        country = None
        try:
            country = CountrySerializer(CountryData.objects.get(pk=pk), exclude_fields=True).data
            return JsonResponse({'country':country, 'message':'Success','status':200})
        except:
            pass        
        return JsonResponse({'country':country, 'message':'Country Not found','status':404})
        
class SaveCountry(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    @extend_schema(request=CountrySerializer)
    def post(self, request):
        try:
            if CountryData.objects.filter(cca2_name=request.data["cca2"]).exists():
                return JsonResponse({'message':'Country already exists','status':210})
            request.data["updated_by"] = request.user.pk
            request.data["updated_at"] = timezone.now()
            serializer = CountrySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Success','status':200})
        except Exception as e:
            print(e)
            pass
        return JsonResponse({'message':'Could not save data','status':500})

class UpdateCountry(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk):
        try:
            country = CountryData.objects.get(pk=pk)
            if CountryData.objects.filter(cca2_name=request.data["cca2"]).exclude(pk=pk).exists():
                return JsonResponse({'message':'Country already exists','status':210})
            request.data["updated_by"] = request.user.pk
            request.data["updated_at"] = timezone.now()
            serializer = CountrySerializer(country, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Success','status':200})
            return JsonResponse({'message':serializer.errors,'status':400})
        except CountryData.DoesNotExist:
            return JsonResponse({'message':'Country does not exist','status':404})
        except Exception as e:
            print(e)
            pass
        return JsonResponse({'message':'Could not save data','status':500})

class DeleteCountry(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def delete(self, request, pk):
        try:
            CountryData.objects.get(pk=pk).delete()
            return JsonResponse({'message':'Success','status':200})
        except:
            pass
        return JsonResponse({'message':'Country Not found','status':404})