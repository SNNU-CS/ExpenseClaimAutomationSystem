# from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers

from utils.exceptions import ValidationError
from utils.message import ErrorMsg

from .models import Organization, Role, Token, User


class UserSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField(read_only=True)
    roles = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        exclude = ('password', )

    def get_roles(self, obj):
        return [{'name': role.name, 'id': role.id} for role in obj.user_roles.all()]

    def get_organization(self, obj):
        organization = obj.organization
        return {
            'org_name': organization.org_name,
            'id': organization.id
        } if organization else {
            'org_name': '',
            'id': None
        }


class CreateUserSerializer(serializers.ModelSerializer):
    roles = serializers.ListField(child=serializers.IntegerField(), required=False)

    def create(self, validated_data):
        roles = validated_data.pop('roles')
        user = User.objects.create(**validated_data)
        user.user_roles.set(roles)
        return user

    def to_representation(self, obj):
        return UserSerializer(obj).data

    class Meta:
        model = User
        exclude = ('is_active', )
        read_only_fields = ['date_joined', 'last_login']


class UpdateUserSerializer(serializers.ModelSerializer):
    roles = serializers.ListField(child=serializers.IntegerField(), required=False)

    def update(self, instance, validated_data):
        roles = validated_data.pop('roles')
        instance.user_roles.set(roles)
        return super().update(instance, validated_data)

    def to_representation(self, obj):
        return UserSerializer(obj).data

    class Meta:
        model = User
        exclude = ('username', 'password')
        read_only_fields = ['date_joined', 'last_login']


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError(ErrorMsg.PASSWORD_MISMATCH)
        return data


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        exclude = ('user', )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    user = UserSerializer(read_only=True)
    token = serializers.CharField(read_only=True)

    def create(self, validated_data):
        token = Token.objects.create(user=validated_data['user'])
        validated_data['token'] = token.token
        return token


class RoleSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Role
        fields = '__all__'

    def get_users(self, obj):
        return [_.username for _ in obj.users.all()]


class OrganizationSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'

    def get_users(self, obj):
        return [_.username for _ in obj.organization_users.all()]
