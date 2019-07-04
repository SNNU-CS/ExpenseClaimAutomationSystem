# from django.shortcuts import render
from django.views import View


class UserAuthView(View):
    def __init__(self, *args):
        super(UserAuthView, self).__init__(*args))
