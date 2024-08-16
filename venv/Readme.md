## FastAPI Hacker News API

### Setup

1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

### Running the Application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
