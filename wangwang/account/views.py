from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.drf import destroy as _destroy
from utils.drf import get_object as _get_object
from utils.exceptions import (
    OrganizationDoesNotExist, PasswordIncorrect, RoleDoesNoeExist, UserIsNotActive, UsertDoesNotExist, ValidationError
)

from .models import Organization, Role, User
from .serializers import (
    ChangePasswordSerializer, CreateUserSerializer, LoginSerializer, OrganizationSerializer, RoleSerializer,
    UpdateUserSerializer, UserSerializer
)
from .signals import user_logged_in


class AuthView(generics.GenericAPIView):
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        query = User.objects.filter(username=username)
        if query.count() == 0:
            raise UsertDoesNotExist
        user = query.get()
        if user.is_active is False:
            raise UserIsNotActive
        if not user.authenticate(password):
            raise PasswordIncorrect
        serializer.save(user=user)
        user_logged_in.send(sender=user.__class__, user=user)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = UserSerializer
    queryset = User.objects.all()
    exc = UsertDoesNotExist

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        elif self.action == 'update':
            return UpdateUserSerializer
        elif self.action == 'set_password':
            return ChangePasswordSerializer
        return super().get_serializer_class()

    def get_object(self):
        return _get_object(self)

    def destroy(self, request, pk=None):
        return _destroy(self, request)

    @action(detail=True, methods=['post'], url_path="password")
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response('password set success')
        else:
            return Response(serializer.errors)


class RoleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']

    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    exc = RoleDoesNoeExist

    def get_object(self):
        return _get_object(self)

    def destroy(self, request, pk=None):
        return _destroy(self, request)


class OrganizationViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'options']
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    exc = OrganizationDoesNotExist

    def get_object(self):
        return _get_object(self)

    def destroy(self, request, pk=None):
        return _destroy(self, request)
