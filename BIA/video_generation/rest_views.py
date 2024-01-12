from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from video_generation.helpers.video_generation_helpers import VideoGenerationHelper


class VideoGenerationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            temp_resp = VideoGenerationHelper().generate_sample_video()
            resp = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': 'Successfully created a sample video.',
                'results': temp_resp
            }
            response_object = Response(resp, status=status.HTTP_201_CREATED)
        except Exception as e:
            resp = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'status_message': str(e),
                'results': {}
            }
            response_object = Response(resp, status=status.HTTP_404_NOT_FOUND)

        return response_object
