#!/usr/bin/env python
"""Initialization script for development environment"""
import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a shell command and handle errors"""
    print(f"\n📦 {description}...")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Error: {description} failed")
        sys.exit(1)
    print(f"✅ {description} completed")

def setup_dev_environment():
    """Setup development environment"""
    print("\n" + "="*50)
    print("SOC Vision Academy - Development Setup")
    print("="*50)
    
    # Check Python version
    print("\n🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print(f"❌ Python 3.9+ required. Found {version.major}.{version.minor}")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor} detected")
    
    # Create virtual environment if it doesn't exist
    if not os.path.exists('venv'):
        run_command('python -m venv venv', 'Creating virtual environment')
    else:
        print("\n✅ Virtual environment already exists")
    
    # Activate virtual environment
    if os.name == 'nt':  # Windows
        activate_cmd = 'venv\\Scripts\\activate && '
    else:  # Unix/Linux/Mac
        activate_cmd = 'source venv/bin/activate && '
    
    # Install dependencies
    run_command(f'{activate_cmd}pip install --upgrade pip', 'Upgrading pip')
    run_command(f'{activate_cmd}pip install -r requirements.txt', 'Installing dependencies')
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        run_command('cp .env.example .env', 'Creating .env file')
        print("   ⚠️  Please update .env with your configuration")
    else:
        print("\n✅ .env file already exists")
    
    # Create uploads directory
    os.makedirs('uploads', exist_ok=True)
    print("\n✅ Uploads directory ready")
    
    # Seed database
    print("\n" + "="*50)
    print("Initializing Database")
    print("="*50)
    run_command(f'{activate_cmd}python seed.py', 'Seeding database with sample data')
    
    # Final instructions
    print("\n" + "="*50)
    print("✅ Setup Complete!")
    print("="*50)
    print("\n🚀 To start the development server:")
    if os.name == 'nt':  # Windows
        print("   1. Run: venv\\Scripts\\activate")
    else:  # Unix/Linux/Mac
        print("   1. Run: source venv/bin/activate")
    print("   2. Run: python app.py")
    print("\n🌐 Application will be available at: http://localhost:5000")
    print("\n📚 Default Credentials:")
    print("   Admin Username: admin")
    print("   Admin Password: Admin@123")
    print("\n💡 Analyst test accounts available (analyst1-analyst5)")
    print("   Password: Password@123")

if __name__ == '__main__':
    setup_dev_environment()
