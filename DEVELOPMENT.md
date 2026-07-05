# SOC Vision Academy - Development Guide

## Quick Start

### Prerequisites
- Python 3.9+
- pip
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Bharathikumar77/SOC-Vision-Academy.git
cd SOC-Vision-Academy

# Run setup script (automatic installation and database seeding)
python setup.py
```

### Manual Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix/Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Seed database with sample data
python seed.py

# Run application
python app.py
```

## Testing Credentials

### Admin Account
- **Username:** admin
- **Password:** Admin@123
- **Access:** Full admin panel and all features

### Test Analyst Accounts
- **Username:** analyst1 through analyst5
- **Password:** Password@123
- **Access:** Regular user features with sample data pre-populated

## Project Structure

```
SOC-Vision-Academy/
├── app/
│   ├── __init__.py                 # Flask app factory
│   ├── models/                     # Database models
│   │   ├── user.py                 # User, Profile, Achievements
│   │   ├── learning.py             # Courses, Lessons, Paths
│   │   ├── investigation.py        # Investigation rooms, Questions
│   │   ├── progress.py             # User progress tracking
│   │   ├── gamification.py         # Badges, Levels, Leaderboard
│   │   └── notification.py         # User notifications
│   ├── routes/                     # Blueprint routes
│   │   ├── auth.py                 # Authentication
│   │   ├── dashboard.py            # Dashboard pages
│   │   ├── profile.py              # User profiles
│   │   ├── learning.py             # Learning pages
│   │   ├── investigation.py        # Investigation pages
│   │   ├── api.py                  # REST API endpoints
│   │   └── admin.py                # Admin panel
│   ├── templates/                  # HTML templates
│   │   ├── base.html               # Base template
│   │   ├── auth/                   # Auth templates
│   │   ├── dashboard/              # Dashboard templates
│   │   ├── profile/                # Profile templates
│   │   ├── learning/               # Learning templates
│   │   ├── investigation/          # Investigation templates
│   │   └── admin/                  # Admin templates
│   ├── static/                     # Static files
│   │   ├── css/                    # Stylesheets
│   │   ├── js/                     # JavaScript files
│   │   └── images/                 # Images and assets
│   ├── utils/                      # Utility functions
│   └── services/                   # Business logic services
├── app.py                          # Application entry point
├── config.py                       # Configuration management
├── seed.py                         # Database seeding script
├── setup.py                        # Development setup script
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment template
└── README.md                       # Project documentation
```

## Features Implemented

### ✅ Core Features
- User authentication with secure password hashing
- Role-based access control (Admin/User)
- User profiles with extended information
- Secure session management

### ✅ Learning Management
- Learning paths for structured learning
- Courses with lessons
- Progress tracking
- Multiple learning progressions

### ✅ Investigation Rooms
- Realistic cyber security scenarios
- Multi-choice and short-answer questions
- Evidence files for analysis
- IOC (Indicator of Compromise) extraction
- MITRE ATT&CK mapping
- Difficulty levels (Beginner to Expert)
- Time estimates and prerequisites

### ✅ Gamification System
- XP (Experience Points) system
- Level progression (1-20)
- Badges and achievements
- Leaderboard with rankings
- Real-time statistics

### ✅ User Dashboard
- Overview of progress
- Featured investigations
- Recent activity
- Notifications
- Statistics page

### ✅ Admin Panel
- User management
- Investigation room creation/editing
- System statistics
- Quick actions

### ✅ REST API
- User statistics endpoint
- Room listing with filtering
- Leaderboard data
- Health check endpoint

## Database Models

### User Management
- `User` - Core user account
- `UserProfile` - Extended user information
- `UserAchievement` - Badges earned

### Learning
- `LearningPath` - Course groupings
- `Course` - Individual courses
- `Lesson` - Lesson content

### Investigations
- `InvestigationRoom` - Scenario definitions
- `Question` - Investigation questions
- `QuestionOption` - Multiple choice options
- `Evidence` - Evidence files
- `IOC` - Indicators of Compromise

### Progress & Gamification
- `UserProgress` - Course progress
- `RoomCompletion` - Investigation completion tracking
- `QuestionAnswer` - Individual question answers
- `Badge` - Badge definitions
- `Level` - Level progression
- `Leaderboard` - Rankings

### Communication
- `Notification` - User notifications

## Environment Variables

```
FLASK_ENV=development              # development, production, testing
FLASK_APP=app.py
SECRET_KEY=your-secret-key        # Change in production
DEV_DATABASE_URL=sqlite:///soc_vision.db
DATABASE_URL=postgresql://...     # Production database
```

## Running the Application

### Development Mode
```bash
# Activate virtual environment
source venv/bin/activate

# Set development mode
export FLASK_ENV=development

# Run the app
python app.py
```

### Production Mode
```bash
# Use gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

### Authentication
- `GET /auth/login` - Login page
- `POST /auth/login` - Process login
- `GET /auth/register` - Registration page
- `POST /auth/register` - Process registration
- `GET /auth/logout` - Logout

### Dashboard
- `GET /dashboard/` - Main dashboard
- `GET /dashboard/stats` - Statistics page

### Learning
- `GET /learning/` - Browse learning paths
- `GET /learning/path/<id>` - View learning path
- `GET /learning/course/<id>` - View course
- `GET /learning/lesson/<id>` - View lesson

### Investigations
- `GET /investigation/` - Browse investigation rooms
- `GET /investigation/room/<id>` - Room details
- `GET /investigation/room/<id>/investigate` - Start investigation
- `POST /investigation/api/submit-answer` - Submit answer

### Admin
- `GET /admin/` - Admin dashboard
- `GET /admin/rooms` - Manage rooms
- `GET /admin/room/new` - Create room
- `GET /admin/room/<id>/edit` - Edit room
- `GET /admin/users` - Manage users

### API
- `GET /api/user/stats` - User statistics
- `GET /api/rooms` - List rooms
- `GET /api/leaderboard` - Leaderboard data
- `GET /api/health` - Health check

## Development Tips

1. **Database**: SQLite in development, PostgreSQL in production
2. **Debugging**: Enable `DEBUG=True` in development config
3. **Testing**: Run tests with pytest
4. **Migrations**: Use Flask-Migrate for schema changes
5. **Static Files**: CSS and JS are in `/app/static`

## Troubleshooting

### Database Issues
```bash
# Reset database
rm soc_vision.db
python seed.py
```

### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Port Already in Use
```bash
# Use different port
python app.py --port 5001
```

## Next Steps

1. Customize investigation scenarios
2. Add more learning content
3. Integrate with real threat intelligence APIs
4. Deploy to cloud platform
5. Setup CI/CD pipeline

## Support

For issues or questions, please create an issue on GitHub.

## License

MIT License - See LICENSE file
