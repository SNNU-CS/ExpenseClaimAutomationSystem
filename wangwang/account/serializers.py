from rest_framework import serializers

from utils.exceptions import PasswordIncorrect, UsertDoesNotExist

from .models import Token, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password')


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    user = UserSerializer(read_only=True)
    token = TokenSerializer(read_only=True)

    def create(self, validated_data):
        token = Token.objects.create(user=validated_data['user'])
        validated_data['token'] = token
        return validated_data

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        query = User.objects.filter(username=username)
        if query.count() == 0:
            raise UsertDoesNotExist
        user = query.get()
        if not user.authenticate(password):
            raise PasswordIncorrect
        attrs['user'] = user
        return super().validate(attrs)
