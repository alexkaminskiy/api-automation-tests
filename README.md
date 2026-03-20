# API Automation Tests

This project is an API automation test suite using pytest, Requests, and Allure.

## Setup


## Virtual Environment Setup

It is recommended to use a virtual environment to manage dependencies.

### Windows
1. Create a virtual environment:
   ```bash
   py -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate

### MacOS/Linux
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Run tests and generate Allure report
1. Configure `config/config.yaml` or set environment variable `API_BASE_URL`.

2. Run tests:
   ```bash
   pytest --alluredir=reports
   ```

2. Generate Allure report:
   ```bash
   allure serve reports
   ```

Notes
- `tests/conftest.py` provides a `client` fixture returning an `APIClient`.
- `src/api_client.py` is a thin wrapper over `requests.Session` that stores the last response for debugging/attachments.
- On test failure the last response body is attached to Allure results automatically.
