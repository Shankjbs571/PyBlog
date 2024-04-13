# PyBlog

PyBlog is a FastAPI application for managing a simple blog system with user authentication and post management features.

## Application Requirements

### Endpoints

#### /auth/signup Endpoint

- Accepts `email` and `password`.
- Returns a token (JWT or randomly generated string).

#### /auth/login Endpoint

- Accepts `email` and `password`.
- Returns a token upon successful login; error response if login fails.

#### /api/posts AddPosts Endpoint

- Accepts `text` and a `token` for authentication.
- Validates payload size (limit to 1 MB), saves the post in memory, returning `postID`.
- Returns an error for invalid or missing token.
- Dependency injection for token authentication.

#### /auth/posts GetPosts Endpoint

- Requires a token for authentication.
- Returns all user's posts.
- Implements response caching for up to 5 minutes for the same user.
- Returns an error for invalid or missing token.
- Dependency injection for token authentication.

#### /api/posts/{posts_id}  Delete post Endpoint

- Accepts `postID` and a `token` for authentication.
- Deletes the corresponding post from memory.
- Returns an error for invalid or missing token.
- Dependency injection for token authentication.

### Additional Features
- Uses in-memory caching for "GetPosts" to cache data for up to 5 minutes, employing tools like `cachetools` for this purpose.
- Ensures the implementation of both SQLAlchemy and Pydantic models for each endpoint includes extensive type validation to guarantee the accuracy and integrity of data being processed.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/your_username/pyblog.git

2. Install the Dependencies:

   ```sh
   pip install -r requirements.txt

3. Create MySQL databse:
   -Create a MySQL database and user (if not already done) and update database.py with your MySQL database configuration.

4. Run the Application:

   ```sh
   python app/main.py

-Access the API at http://localhost:8000 in your browser.


  
