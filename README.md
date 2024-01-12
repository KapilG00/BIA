# Boston Institute Of Analytics

## Overview

Developed a simple web app using Django and Django REST Framework. This
system will handle collection of books (CRUD), also added the video generation feature using moviepy.

## Setup

### Prerequisites

Make sure you have the following installed:

- Python (version 3.11.3)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KapilG00/BIA.git
    ```

2. Navigate to the project directory:

    ```bash
    cd BIA
    ```

3. Create and activate a virtual environment (optional but recommended):
    
    ```bash
    virtualenv venv
    ```

    ```bash
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Install database (recommended Postgresql):
   
   ### Below commands are specific to Postgresql, make necessary changes if any.

   After successful installation, login to psql-shell/Terminal to create database using following commands:

   ```bash
   CREATE ROLE BIA;
   ```
   ```bash
   ALTER ROLE BIA WITH PASSWORD 'BIA';
   ```
   ```bash
   ALTER ROLE BIA WITH LOGIN;
   ```
   ```bash
   CREATE DATABASE BIA WITH OWNER BIA;
   ```
   ```bash
   GRANT ALL PRIVILEGES ON DATABASE BIA TO BIA;
   ```

6. Apply database migrations and create Superuser:

    ```bash
    python manage.py migrate
    ```

    ```bash
    python manage.py createsuperuser
    ```
    
### Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

### API Endpoints
### 1. User Login : /auth/user-login/

    This view allows users to Log In and obtain authentication tokens.

    Method : POST

    Request Body :

    {
        "email": "test@example.com",
        "password": "testpassword"
    }
    
### 2. User Registration : /auth/user-registration/

    This view allows users to register and create a new account.

    Method : POST

    Request Body :

    {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword"
    }

### 3. Fetching all book's : /books/books_crud/

    This view allows user to retrieve details of all book's.

    Method : GET

### 4. Adding a book : /books/books_crud/

    This view allows user to add a new book.

    Method : POST

    Request Body :

    {
        "book_id": "101",
        "title": "book title",
        "author": "k1",
        "publication_date": "2021-01-23",
        "genre": "Horror",
        "rating": 3.94,
        "num_pages": 245
     }

### 5. Updating a book details : /books/books_crud/{book_id}/

    This view allows user to update book details.

    Method : PUT

    Request Body :

    {
        "title": "new book title",
        "author": "k1",
        "publication_date": "2021-11-14",
        "genre": "Horror",
        "rating": 4.15,
        "num_pages": 300
    }

### 6. Deleting a book : /books/books_crud/{book_id}/

    This view allows user to delete already existing book'.

    Method : DELETE

### 7. Generating a video using moviepy : /moviepy/video_gen/

    This view allows user to create a sample video.

    Method : POST
    
## Contact
For questions or feedback, please email me at kapil.gupta4949@gmail.com.
