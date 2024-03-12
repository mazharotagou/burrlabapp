import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

# Get the port number from an environment variable or use a default value (8080)
port = int(os.environ.get("PORT", 8080))

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)