# FastAPI Project #2
This project is an API built with FastAPI that handles API requests and interacts with a database. It utilizes SQLAlchemy for ORM-based database management and Pydantic for data validation.

## Technologies Used
- **Python**
- **FastAPI**
- **SQLAlchemy**
- **Docker**

## Project Structure
- **main.py**: Main application entry point.
- **database.py**: Database connection setup.
- **repository.py**: Contains CRUD operations.
- **schemas.py**: Defines data models.
- **router.py**: API routes.
- **Dockerfile**: Application containerization.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/youngroma/FastAPI-project2.git
```
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Run the app:
```bash
uvicorn main:app --reload
```
