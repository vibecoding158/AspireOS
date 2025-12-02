from flask import Flask, render_template_string

app = Flask(__name__)

# Import your HTML template from main.py
# For now, we'll create a minimal version
@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AspireOS Dashboard</title>
        <style>
            body { font-family: system-ui; padding: 20px; }
        </style>
    </head>
    <body>
        <h1>AspireOS Dashboard</h1>
        <p>Serverless version - Full HTML would go here</p>
    </body>
    </html>
    """
    return render_template_string(html)

# Vercel serverless handler
def handler(request):
    return app(request.environ, lambda status, headers: None)

