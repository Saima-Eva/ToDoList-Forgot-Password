from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

class emailbackEnd(ModelBackend):
    def authenticate(self,  username=None, password=None, **args):
        usermodel=get_user_model()
        
        try:
            user=usermodel.objects.get(email=username)
        except usermodel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None