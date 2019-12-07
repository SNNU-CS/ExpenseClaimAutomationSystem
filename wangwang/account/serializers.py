from rest_framework import serializers

from .models import Token, User


class UserSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('id', 'password')

    def get_organization(self, obj):
        return obj.organization.org_name if obj.organization else None


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        exclude = ('id', 'user')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    user = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    # in order to use serializer.save(user=user, token=token)
    def create(self, validated_data):
        return validated_data

    def get_token(self, obj):
        return obj['token'].token

    def get_user(self, obj):
        data = UserSerializer(obj['user']).data
        del data['is_active']
        del data['username']
        return data
