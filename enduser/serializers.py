
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import CustomUser, Pin, Profile
from .exception import EmailNotValid

    
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
        try:
            pin = Pin.objects.get(email=data['email'])
            if not pin:
               raise serializers.ValidationError("Invalid OTP or OTP expired")
            if pin.otp != data["otp"]:
               pin.attempt_count +=1
               pin.save()
               raise serializers.ValidationError('Invalid OTP')
          
            pin.delete()
            return data
        except Pin.DoesNotExist :
            raise serializers.ValidationError("Email is not valid")
          
          

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
   