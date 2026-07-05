#!/usr/bin/env python
"""
WSGI entry point for production servers (Render/gunicorn).

This file exists separately from app.py because the project also has an
`app/` package directory. gunicorn's module-based target resolves `app`
to that package (Python prefers packages over same-named modules), not
to app.py, which breaks a start command like `gunicorn app:app`.
Pointing gunicorn at wsgi.py instead sidesteps the collision entirely.
"""
import os
from dotenv import load_dotenv

load_dotenv()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
