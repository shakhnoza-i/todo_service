from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from accounts.serializers import RegistrationSerializer


class LogoutView(APIView):
    
    def post(self, request, format=None):
        logout(request)
        data = {"You are now logged out."}
        return Response(data, status=status.HTTP_200_OK)


class RegistrationView(APIView):

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data = request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful!"
            data['email'] = account.email

            refresh = RefreshToken.for_user(account)
            
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }

        else:
            data = serializer.errors

        return Response(data)


class LoginView(APIView):

    def post(self, request, format=None):
        data = {}
        email = request.POST['email']
        password = request.POST['password']
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):       
                refresh = RefreshToken.for_user(user)
                data['token'] = {
                                    'refresh': str(refresh),
                                    'access': str(refresh.access_token),
                                }
                return Response(data)      
            else:
                data = 'Wrong username or password!'
