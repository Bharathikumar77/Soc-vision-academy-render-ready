#!/usr/bin/env python
"""Migration initialization script"""
from dotenv import load_dotenv

load_dotenv()

from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        print("Creating initial migration...")
        # This would be run: flask db init, flask db migrate, flask db upgrade
        print("Run: flask db init")
        print("Run: flask db migrate")
        print("Run: flask db upgrade")
