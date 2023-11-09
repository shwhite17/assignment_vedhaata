from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile']

class UserLoginSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    otp = serializers.CharField()
