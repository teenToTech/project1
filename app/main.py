import os
from flask import Flask

app = Flask(__name__)

# Read greeting from environment variable
greeting = os.environ.get("GREETING", "Hello World!")

@app.route("/")
def hello():
    return greeting

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
