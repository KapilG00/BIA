from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class AuthenticationHelper:    
    def __init__(self):
        pass

    def login_user(self, data):
        email = data.get('email', None).lower()
        password = data.get('password', None)

        if not email or not password:
            raise Exception('Both email and password are mandatory.')
        
        # Authenticating user.
        user_obj = authenticate(email=email, password=password)

        if not user_obj:
            raise Exception('Please provide valid login credentials.')
        user_details = {
            "username": user_obj.username,
            "email": user_obj.email
        }
        # Generating access and refresh tokens using simple-jwt.
        refresh_token = RefreshToken.for_user(user_obj)
        access_token = refresh_token.access_token

        response_object = {
            "access_token": str(access_token),
            "refresh_token": str(refresh_token),
            "user_details": user_details
        }

        return response_object

    def register_user(self, data):
        username = data.get('username', None).lstrip()
        email = data.get('email', None).lower().lstrip()
        password = data.get('password', None).lstrip()
        try:
            user = User.objects.get(email=email)
            if user is not None:
                raise Exception('User already registered.')
        except User.DoesNotExist:
            # Registering a user.
            user_obj = User.objects.create(username=username, email=email, password=password)
            user_obj.set_password(password)
            user_obj.save()
        except Exception as e:
            raise Exception(e)
        
        user_details = {
            "username": user_obj.username,
            "email": user_obj.email
        }

        return user_details