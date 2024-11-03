import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set any environment variables if needed
os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application  # Assuming the main file is named "app.py"
