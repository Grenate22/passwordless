from rest_framework.decorators import api_view,action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import CustomUser, Pin, Profile
from .serializers import EmailSerializer,RegisterVerifySerializer, ProfileSerializer, UserSerializer
from .send_mail import send_verification_email
from .token import get_tokens_for_user
from .permission import IsFullyAuthenticated


class RegistrationViewSet(ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]

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
            return Response({"message":"Otp sent succesfully"})
        return (serializer.errors)
    
    @action(detail=False, methods=['post'])
    def verfiy_otp(self,request):
        serializer = RegisterVerifySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            user, created = CustomUser.objects.get_or_create(email=email)
            if user:
                token = get_tokens_for_user(user=user)
                print(token['access'])
                print(token['refresh'])
                return Response({"access":token['access'],"refresh":token['refresh']})
            else:

                return Response({"message":"Otp Error"})

        return Response(serializer.errors)
    
class ProfileViewSet(ModelViewSet):
    http_method_names = ['get','put','delete']
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    def get_queryset(self):
        user = self.request.user
        user_id = CustomUser.objects.get(id=user.id)
        profile = Profile.objects.filter(user=user_id)
        return profile
    
    def get_serializer_context(self):
        return {"user_id":self.request.user.id}
    
class UserViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class CustomView(APIView):
    permission_classes = [IsFullyAuthenticated]

    def get(self,request):
        domain = request.get_host().split(":")[0]
        print(f"hello {domain}")
        return Response({"message":domain})
    
