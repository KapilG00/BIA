from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .helpers.authentication_helpers import AuthenticationHelper


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        user_data = request.data
        try:
            temp_resp = AuthenticationHelper().login_user(user_data)
            resp = {
                'status_code': status.HTTP_200_OK,
                'status_message': 'Logged In Successfully.',
                'results': temp_resp
            }
            response_object = Response(resp, status=status.HTTP_200_OK)
        except Exception as e:
            resp = {
                'status_code': status.HTTP_401_UNAUTHORIZED,
                'status_message': str(e),
                'results': {}
            }
            response_object = Response(resp, status=status.HTTP_401_UNAUTHORIZED)

        return response_object    
                 

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        user_data = request.data
        try:
            temp_resp = AuthenticationHelper().register_user(user_data)
            resp = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': 'Registration Successful.',
                'results': temp_resp
            }
            response_object = Response(resp, status=status.HTTP_201_CREATED)
        except Exception as e:
            resp = {
                'status_code': status.HTTP_409_CONFLICT,
                'status_message': str(e),
                'results': {}
            }
            response_object = Response(resp, status=status.HTTP_409_CONFLICT)

        return response_object    