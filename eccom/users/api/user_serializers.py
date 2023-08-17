
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=True,write_only=True)
    password = serializers.CharField(required=True,write_only=True)
    confirm_password = serializers.CharField(required=True,write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff','password','confirm_password',]
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        user =  User.objects.create_user(**validated_data)
        if user:
            user.set_password(password)
        return user
    def update(self, instance, validated_data):
        user = instance
        user.username = validated_data.get('username', user.username)
        user.email = validated_data.get('email', user.email)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.is_staff = validated_data.get('is_staff', user.is_staff)
        user.save()
        if validated_data.get("password"):
            user.set_password(validated_data.get("password"))  
        user.save()
        return user 

