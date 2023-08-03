from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackEnd(ModelBackend):
    def authenticate(self, username = None, password = None, **kwrgs):
        userModel = get_user_model()
        
        try:
            user = userModel.objects.get(email=username)
            
        except userModel.DoesNotExist:
            return None
        
        else:
            if user.check_password(password):
                return user
        
        return None