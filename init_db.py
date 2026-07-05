#!/usr/bin/env python
"""
Idempotent database setup for production (Render build step).
Creates tables if missing, and seeds demo data only on the very first run
(checked by looking for the admin user) so redeploys don't wipe real users.
"""
from dotenv import load_dotenv
load_dotenv()

from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()
    already_seeded = User.query.filter_by(username='admin').first() is not None

if already_seeded:
    print("Database already initialized — skipping seed.")
else:
    print("First run detected — seeding database...")
    import subprocess, sys
    subprocess.run([sys.executable, "seed.py"], check=True)
