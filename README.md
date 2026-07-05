# SOC Vision Academy

A comprehensive and innovative cybersecurity learning platform designed for blue team analysts and SOC professionals. SOC Vision Academy provides hands-on, practical training through realistic investigation scenarios and enterprise environments.

## Features

- 🔐 **User Authentication & Profiles** - Secure account management with role-based access
- 📚 **Learning Paths** - Structured courses from beginner to advanced
- 🔍 **Investigation Rooms** - Realistic scenarios with enterprise environments
- 📊 **SIEM-Style Analysis** - Log analysis and evidence examination
- 🎯 **Gamification** - XP, Levels, Badges, and Leaderboards
- 📈 **Progress Tracking** - Comprehensive learning metrics
- 🛡️ **MITRE ATT&CK Mapping** - Industry-standard attack framework
- 🔔 **Notifications** - Real-time updates on achievements
- ⚙️ **Admin Panel** - Complete platform management
- 🔗 **REST API** - Complete API for integrations

## Technology Stack

- **Backend:** Python Flask with SQLAlchemy ORM
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Database:** SQLite (Development), PostgreSQL (Production)
- **Architecture:** Enterprise-grade modular design

## Project Structure

```
SOC-Vision-Academy/
├── app.py
├── config.py
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   ├── static/
│   └── utils/
├── uploads/
└── migrations/
```

## Quick Start

### Prerequisites
- Python 3.9+
- pip
- Virtual environment

### Installation

```bash
# Clone repository
git clone https://github.com/Bharathikumar77/SOC-Vision-Academy.git
cd SOC-Vision-Academy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Initialize database
flask db upgrade

# Run application
flask run
```

Application will be available at `http://localhost:5000`

## License

MIT License - See LICENSE file for details

## Author

Bharathikumar77
