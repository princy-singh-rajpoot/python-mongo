
# CRUD Operations on Vendor Model

This project demonstrates CRUD (Create, Read, Update, Delete) operations on a Vendor model using FastAPI as the web framework, MongoDB as the database, and Uvicorn as the ASGI server.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
- **MongoDB**: A NoSQL database program that uses JSON-like documents with optional schemas.
- **Uvicorn**: A lightning-fast ASGI server implementation.

## Requirements

- FastAPI
- MongoDB
- Uvicorn

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup MongoDB:**
    - Make sure MongoDB is installed and running on your machine. 
    - You can download MongoDB from [here](https://www.mongodb.com/try/download/community).

## Running the Application

1. **Start the Uvicorn server:**
    ```bash
    uvicorn index:app --reload
    ```

2. **Access the API documentation:**
    - Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the interactive API documentation provided by Swagger UI.

## API Endpoints

- **Create Vendor**: `POST /vendors/`

- **Read All Vendors**: `GET /vendors/`

- **Read Single Vendor**: `GET /vendors/{vendor_id}`

- **Update Vendor**: `PATCH /vendors/{vendor_id}`

- **Delete Vendor**: `DELETE /vendors/{vendor_id}`
