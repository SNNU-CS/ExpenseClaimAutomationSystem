from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# class UserAuthView(View):
#     def __init__(self, *args):
#         super(UserAuthView, self).__init__(*args))


def login(request):
    print(request)
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.filter(username=username)
    except User.DoseNotExist:
        return JsonResponse({})
    password = User.check_password(password)
    if not password:
        return JsonResponse({"status": 401, "msg": "密码错误", 'data': ''})
    else:
        data = {
            'username': username,
            'token': 'test token'
        }
        return JsonResponse({"status": 200, "msg": "登录成功", 'data': data})
