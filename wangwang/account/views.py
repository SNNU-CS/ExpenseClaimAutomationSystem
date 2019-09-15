from .models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
# class UserAuthView(View):
#     def __init__(self, *args):
#         super(UserAuthView, self).__init__(*args))


def login(request):
    body = json.loads(request.body)
    username = body.get('username')
    password = body.get('password')
    try:
        user = User.objects.get(username=username)
    except Exception:
        return JsonResponse({"status": 1000, "msg": "用户不存在", 'data': ''})
    # if username is not 'admin':
    #     return JsonResponse({"status": 1000, "msg": "用户不存在", 'data': ''})
    user = authenticate(username=username, password=password)
    if user is None:
        # 先假装登录成功，以后记得把200改成401
        return JsonResponse({"status": 200, "msg": "密码错误", 'data': ''})
    else:
        data = {
            'username': username,
            'token': 'test token'
        }
        return JsonResponse({"status": 200, "msg": "登录成功", 'data': data})
