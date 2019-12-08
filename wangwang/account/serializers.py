from rest_framework import serializers

from .models import Organization, Role, Token, User


class UserSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField(read_only=True)
    roles = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ('password', )

    def get_organization(self, obj):
        return obj.organization.org_name if obj.organization else None

    def get_roles(self, obj):
        return [_.name for _ in obj.user_roles.all()]


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        exclude = ('user', )


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
