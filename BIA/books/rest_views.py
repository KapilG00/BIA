from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.response import Response
from books.helpers.book_helpers import BookHelper


class BookView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            temp_resp = BookHelper().get_all_books()
            resp = {
                'status_code': status.HTTP_200_OK,
                'status_message': 'Successfully fetched all books.',
                'results': temp_resp
            }
            response_object = Response(resp, status=status.HTTP_200_OK)
        except Exception as e:
            resp = {
                'status_code': status.HTTP_204_NO_CONTENT,
                'status_message': str(e),
                'results': {}
            }
            response_object = Response(resp, status=status.HTTP_204_NO_CONTENT)

        return response_object

    def post(self, request, *args, **kwargs):
        book_data = request.data
        try:
            temp_resp = BookHelper().add_book(book_data)
            resp = {
                'status_code': status.HTTP_201_CREATED,
                'status_message': 'Successfully added a book.',
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
    
    def put(self, request, *args, **kwargs):
        book_data = request.data
        book_id = kwargs.get('book_id')
        try:
            temp_resp = BookHelper().update_book(book_id, book_data)
            resp = {
                'status_code': status.HTTP_200_OK,
                'status_message': 'Successfully updated a book details.',
                'results': temp_resp
            }
            response_object = Response(resp, status=status.HTTP_200_OK)
        except Exception as e:
            resp = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'status_message': str(e),
                'results': {}
            }
            response_object = Response(resp, status=status.HTTP_404_NOT_FOUND)

        return response_object
    
    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        try:
            temp_resp = BookHelper().delete_book(book_id)
            resp = {
                'status_code': status.HTTP_204_NO_CONTENT,
                'status_message': 'Successfully deleted a book.',
                'results': temp_resp
            }
            response_object = Response(resp, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            resp = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'status_message': str(e),
                'results': {}
            }
            response_object = Response(resp, status=status.HTTP_404_NOT_FOUND)

        return response_object