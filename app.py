"""
Pattern Analytics Platform Entrypoint
Supports:
1. Streamlit runtime ('streamlit run app.py') -> Launches dashboard/app.py
2. Vercel / WSGI runtime -> Exports 'app', 'application', 'handler' interfaces
"""
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR / "src"))
sys.path.insert(0, str(ROOT_DIR))

TARGET_APP = ROOT_DIR / "dashboard" / "app.py"

# WSGI Application Handler (Satisfies Vercel Python runtime requirements)
def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Cache-Control', 'public, max-age=3600')
    ]
    start_response(status, headers)
    portal_path = ROOT_DIR / "reports" / "index.html"
    if portal_path.exists():
        with open(portal_path, "rb") as f:
            return [f.read()]
    return [b"<h1>Pattern Analytics Platform</h1><p>Visit /reports/index.html</p>"]

# Standard WSGI aliases for Vercel / AWS / Gunicorn
application = app
handler = app

# If executed directly by Python CLI or Streamlit, launch the dashboard
if __name__ == "__main__" or "streamlit" in sys.modules:
    import runpy
    if TARGET_APP.exists():
        runpy.run_path(str(TARGET_APP), run_name="__main__")
    else:
        raise FileNotFoundError(f"Dashboard app not found at: {TARGET_APP}")
