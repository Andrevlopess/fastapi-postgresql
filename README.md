# FastAPI with PostgreSQL

This project is a simple To-Do application built with FastAPI and PostgreSQL. It demonstrates how to create a RESTful API using FastAPI and interact with a PostgreSQL database.

## Features

- FastAPI for building the API
- PostgreSQL for the database
- SQLAlchemy for ORM
- Alembic for database migrations
- Pydantic for data validation

## Requirements

- Python 3.8+
- PostgreSQL
- Virtualenv

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-postgres-todo.git
    cd fastapi-postgres-todo
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database and update the `DATABASE_URL` in the `.env` file:

    ```env
    DATABASE_URL=postgresql://username:password@localhost/dbname
    ```

5. Run the database migrations:

    ```bash
    alembic upgrade head
    ```

## Running the Application

1. Start the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /todos`: Get a list of all to-dos
- `POST /todos`: Create a new to-do
- `GET /todos/{id}`: Get a to-do by ID
- `PUT /todos/{id}`: Update a to-do by ID
- `DELETE /todos/{id}`: Delete a to-do by ID

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
