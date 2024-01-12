from books.models import Book
from books.serializers import BookSerializer

class BookHelper:  
    def __init__(self):
        pass

    def get_book(self, book_id):
        try:
            book_obj = Book.objects.get(book_id=book_id)
            book_serialized_data = BookSerializer.get_Serialized_JSON(book_obj)
        except Book.DoesNotExist:
            raise Exception(f'Book with {book_id} book id does not exists.')
        except Exception as e:
            raise Exception(str(e))

        return book_serialized_data

    def get_all_books(self):
        try:
            books_list = Book.objects.all()
            if not books_list.exists():
                raise Exception('No books found, please add one.')
            books_serialized_list = BookSerializer.get_Serialized_JSON(books_list)
        except Exception as e:
            raise Exception(str(e))

        return books_serialized_list
    
    def add_book(self, book_data):
        book_id = book_data.get('book_id').lstrip()
        title = book_data.get('title').lstrip()
        author = book_data.get('author').lstrip()
        publication_date = book_data.get('publication_date').lstrip()
        genre = book_data.get('genre').lstrip()
        rating = book_data.get('rating')
        num_pages = book_data.get('num_pages')
        try:
            book_data = Book.objects.create(book_id=book_id, title=title, author=author, publication_date=publication_date,
                                            genre=genre, rating=rating, num_pages=num_pages)
            book_serialized_data = BookSerializer.get_Serialized_JSON(book_data)
            return book_serialized_data
        except Exception as e:
            raise Exception(str(e))

    def update_book(self, book_id, book_data):
        title = book_data.get('title').lstrip()
        author = book_data.get('author').lstrip()
        publication_date = book_data.get('publication_date').lstrip()
        genre = book_data.get('genre').lstrip()
        rating = book_data.get('rating')
        num_pages = book_data.get('num_pages')
        try:
            book_obj = Book.objects.get(book_id=book_id)
            book_obj.title = title
            book_obj.author = author
            book_obj.publication_date = publication_date
            book_obj.genre = genre
            book_obj.rating = rating
            book_obj.num_pages = num_pages
            book_obj.save(update_fields=["title", "author", "publication_date", "genre", "rating", "num_pages"])

            updated_book_data = self.get_book(book_id)
        except Book.DoesNotExist:
            raise Exception(f'Book with {book_id} book id does not exists.')
        except Exception as e:
            raise Exception(str(e))

        return updated_book_data
    
    def delete_book(self, book_id):
        success = False
        try:  
            book_obj = Book.objects.get(book_id=book_id)
            book_obj.delete()
            success = True
        except Book.DoesNotExist:
            raise Exception(f'Book with {book_id} book id does not exists.')
        
        return success