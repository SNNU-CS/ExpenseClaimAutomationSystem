from rest_framework import generics
from rest_framework.response import Response

from utils.exceptions import PasswordIncorrect, UsertDoesNotExist, ValidationError

from .models import Token, User
from .serializers import LoginSerializer
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
        if not user.authenticate(password):
            raise PasswordIncorrect
        token = Token.objects.create(user=user)
        serializer.save(user=user, token=token)
        user_logged_in.send(sender=user.__class__, user=user)
        return Response(serializer.data)


# class UserViewSet(ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
