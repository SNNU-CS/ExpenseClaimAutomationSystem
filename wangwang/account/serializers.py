from rest_framework import serializers

from .models import Organization, Role, Token, User


class UserSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField(read_only=True)
    roles = serializers.SerializerMethodField(read_only=True)
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    sex = serializers.CharField(source='get_sex_display', read_only=True)

    class Meta:
        model = User
        exclude = ('password', )

    def get_roles(self, obj):
        return [_.name for _ in obj.user_roles.all()]


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
