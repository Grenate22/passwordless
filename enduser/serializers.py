from rest_framework import serializers
from datetime import timezone
from .send_mail import send_verification_email
from .utils import generate_pin
from django.core.validators import EmailValidator
from .models import CustomUser, Pin, Profile

    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id","bio","first_name","last_name"]

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Profile.objects.create(user_id=user_id, **validated_data)
    


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = "__all__"


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
   