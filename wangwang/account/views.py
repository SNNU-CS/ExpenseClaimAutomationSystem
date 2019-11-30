from utils.exceptions import PasswordIncorrect, UsertDoesNotExist

from .models import Token, User


def login(request):
    username = request.body.get('username')
    password = request.body.get('password')
    query = User.objects.filter(username=username)
    if query.count() == 0:
        raise UsertDoesNotExist
    user = query.get()
    if user.authenticate(password):
        token = Token.objects.create(user=user)
    else:
        raise PasswordIncorrect
    return {'token': token.token, 'username': username}
