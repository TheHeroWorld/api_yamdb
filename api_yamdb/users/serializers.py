from django.contrib.auth import get_user_model
from rest_framework import serializers
import re

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя не может быть "me"'
            )
        if not re.match(r'^[a-zA-Z0-9_]*$', value):
            raise serializers.ValidationError(
                "Имя пользователя может содержать только буквы,"
                "цифры и символ подчеркивания"
            )
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )

    def validate_role(self, role):
        req_user = self.context['request'].user
        user = User.objects.get(username=req_user)
        if user.is_user:
            role = user.role
        return role
