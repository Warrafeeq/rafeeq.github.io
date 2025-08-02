#!/usr/bin/env python
"""
Deployment script for the Django portfolio website
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description}: {e}")
        print(f"Output: {e.stdout}")
        print(f"Error: {e.stderr}")
        return None

def main():
    """Main deployment function"""
    print("🚀 Starting Django Portfolio Deployment")
    
    # Install dependencies
    run_command("pip install -r requirements.txt", "Installing dependencies")
    
    # Run migrations
    run_command("python manage.py makemigrations", "Creating migrations")
    run_command("python manage.py migrate", "Running migrations")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    # Populate data
    run_command("python populate_data.py", "Populating initial data")
    
    # Copy additional assets
    run_command("python copy_assets.py", "Copying Jekyll assets")
    
    print("\n🎉 Deployment completed successfully!")
    print("\nTo start the development server, run:")
    print("python manage.py runserver")
    print("\nAccess your website at: http://127.0.0.1:8000/")
    print("Admin panel at: http://127.0.0.1:8000/admin/")
    print("Admin credentials: admin / admin123")

if __name__ == "__main__":
    main()