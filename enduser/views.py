from django.shortcuts import render
from datetime import timezone
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import api_view,action
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Pin
from .serializers import EmailSerializer,RegisterVerifySerializer
from .send_mail import send_verification_email
from .token import get_tokens_for_user


class RegistrationViewSet(ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            pin=Pin.objects.filter(email=email)
            if pin:
                pin.delete()
            pin = Pin(email=email)
            pin.generate_save_pin()
            pin.save()
            print(pin.max_otp_try)
            send_verification_email(pin)
            return Response(data=serializer.data)
        return (serializer.errors)
    
    @action(detail=False, methods=['post'])
    def verfiy_otp(self,request):
        serializer = RegisterVerifySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            user, created = CustomUser.objects.get_or_create(email=email)
            if user.is_active==True:
                token = get_tokens_for_user(user=user)
                return Response({"access_token":token.access, "refresh_token":token.refresh})
            elif created or user:
                user.is_active = False

                return Response({"message":"Update your data"})

            return Response({"error":"An unexpected error occured"})
        return Response(serializer.errors)
    
