# Dummy web server to avoid H14 error
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running."

if __name__ == "__main__":
    app.run()
