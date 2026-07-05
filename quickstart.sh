#!/bin/bash
# Quick start script for Unix/Linux/Mac

echo "SOC Vision Academy - Quick Start"
echo "================================="
echo ""

# Check Python
echo "🐍 Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9+"
    exit 1
fi
python3 --version

# Create venv
echo ""
echo "📦 Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate venv
echo ""
echo "🔄 Activating virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment activated"

# Install dependencies
echo ""
echo "📚 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
echo "✅ Dependencies installed"

# Create .env
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ .env file created (update if needed)"
fi

# Create uploads folder
mkdir -p uploads
echo "✅ Uploads folder ready"

# Seed database
echo ""
echo "🗄️  Seeding database..."
python seed.py

echo ""
echo "================================="
echo "✅ Ready to start!"
echo "================================="
echo ""
echo "Run: python app.py"
echo ""
echo "Then open: http://localhost:5000"
echo ""
echo "Admin Login:"
echo "  Username: admin"
echo "  Password: Admin@123"
echo ""
