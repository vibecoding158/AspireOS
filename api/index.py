# api/index.py

from main import app  # 'app' must be the Flask instance defined in main.py

# No handler function needed.
# Vercel detects the `app` variable and runs it as a WSGI app.