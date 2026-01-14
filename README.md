# Learn-Python

This project is a task management application built with FastAPI.

## Project Setup

Follow these steps to set up and run the project locally.

### 1. Prerequisites

- Python 3.12 or higher

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

### 4. Install Dependencies

Install the required Python packages from `requirement.txt`.

```bash
pip install -r requirement.txt
```

### 5. Environment Configuration

Ensure you have a `.env` file in the root directory with the necessary configuration (e.g., `DB_CONNECTION`).

Example `.env` content:
```env
DB_CONNECTION=postgresql://user:password@localhost:5432/dbname
```

### 6. Run the Application

Start the FastAPI server using Uvicorn.

```bash
uvicorn main:app --reload
```

```bash
fastapi dev main.py --reload
```

The application will be available at `http://127.0.0.1:8000`.
API documentation can be accessed at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
