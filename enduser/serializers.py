from rest_framework import serializers
from datetime import timezone
from .send_mail import send_verification_email
from .utils import generate_pin
from django.core.validators import EmailValidator
from .models import CustomUser, Pin, Profile

    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = CustomUser.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user


    
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = CustomUser.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class RegisterVerifySerializer(serializers.ModelSerializer):
     email = serializers.EmailField()
     otp = serializers.CharField(max_length=6)

     class Meta:
         model = Pin
         fields = ['otp','email']
         

     def validate(self, data):
          pin = Pin.objects.get(email=data['email'])
          print(f"pin received from the end {pin.otp}")
          if not pin:
               raise serializers.ValidationError("Invalid OTP or OTP expired")
          
          
          if pin.otp != data["otp"]:
               pin.attempt_count +=1
               pin.save()
               raise serializers.ValidationError('Invalid OTP')
          
          pin.delete()
          return data

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
   