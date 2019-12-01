from rest_framework.response import Response
from rest_framework.views import APIView

from utils.exceptions import ValidationError

from .serializers import LoginSerializer


class AuthView(APIView):
    authentication_classes = []

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.body)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        serializer.save()
        return Response(serializer.data)


# class UserViewSet(ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
