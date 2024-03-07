from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from .serializers import *
from inmest_api.utils import *

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    username = request.data.get('username')
    last_name = request.data.get('last_name')
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    new_user = IMUser.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number
    )

    new_user.set_password(password)
    new_user.save()
    # new_user.generate_auth_token()
    serializer = UserSerializer(new_user, many=False)
    return Response({"message": "Account successfully created", "result": serializer.data})

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    #1. Receive inputs/data from client and validate inputs
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Please provide both username and password"}, status.HTTP_400_BAD_REQUEST)
    
    #2. Check user existence
    try:
        user = IMUser.objects.get(username=username)

        #3. Check user authentication
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            login(request, user)
            serializer = AuthSerializer(user, many=False)
            return Response({"result": serializer.data}, status.HTTP_200_OK)

        else:
            return Response({"error": "Invalid credentials"}, status.HTTP_400_BAD_REQUEST)

    except IMUser.DoesNotExist:
        return Response({"error": "User does not exist"}, status.HTTP_404_NOT_FOUND)
    
    #4. Login user
    #5. Respond to the users request

class ForgotPasswordAPIView(APIView):
    def post(self, request):
        #1. Receive the username(email)
        username = request.data.get('username')
        if not username:
           generate_400_response("Please provide valid username")

        #2. Check if the user exists
        try:
            user = IMUser.objects.get(username=username)
            otp_code = generate_unique_code()

            #3. Send OTP code
        
            user.unique_code = otp_code
            user.save()
            #send email or SMS

            #4. Respond to the user
            return Response({"message": "Please check your email for an OTP code sent"}, status.HTTP_200_OK)

        except IMUser.DoesNotExist:
            generate_400_response("User does not exist")

