API Automation Framework (pytest + requests + allure)

Quick start

1. Create and activate a virtualenv (recommended)

On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure `config/config.yaml` or set environment variable `API_BASE_URL`.

4. Run tests

```bash
pytest
```

5. Generate/serve Allure report (Allure CLI required)

```bash
allure serve reports/allure-results
```

Notes
- `tests/conftest.py` provides a `client` fixture returning an `APIClient`.
- `src/api_client.py` is a thin wrapper over `requests.Session` that stores the last response for debugging/attachments.
- On test failure the last response body is attached to Allure results automatically.
