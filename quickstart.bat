@echo off
REM Quick start script for Windows

echo SOC Vision Academy - Quick Start
echo =================================
echo.

REM Check Python
echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python 3 not found. Please install Python 3.9+
    exit /b 1
)
python --version

REM Create venv
echo.
echo Setting up virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

REM Activate venv
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated

REM Install dependencies
echo.
echo Installing dependencies...
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt >nul 2>&1
echo Dependencies installed

REM Create .env
if not exist ".env" (
    copy .env.example .env
    echo .env file created (update if needed)
)

REM Create uploads folder
if not exist "uploads" (
    mkdir uploads
)
echo Uploads folder ready

REM Seed database
echo.
echo Seeding database...
python seed.py

echo.
echo =================================
echo Ready to start!
echo =================================
echo.
echo Run: python app.py
echo.
echo Then open: http://localhost:5000
echo.
echo Admin Login:
echo   Username: admin
echo   Password: Admin@123
echo.
pause
