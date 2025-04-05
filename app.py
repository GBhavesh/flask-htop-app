from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    return '<h3>Welcome! Visit <a href="/htop">/htop</a> for system info.</h3>'

@app.route("/htop")
def htop():
    # 🔁 Replace with your real name
    name = "Bhavesh Gupta"

    try:
        username = os.getlogin()
    except:
        username = os.environ.get("USER", "codespace")

    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    time_ist = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")

    # Get top output
    top_output = subprocess.getoutput("top -b -n1 | head -n 30")

    return f"""
    <html>
    <head>
        <title>/htop</title>
        <style>
            body {{
                font-family: monospace;
                background-color: #f9f9f9;
                padding: 20px;
            }}
            .block {{
                margin-bottom: 10px;
            }}
            .top-box {{
                background-color: #fff;
                border: 1px solid #ccc;
                padding: 10px;
                white-space: pre-wrap;
                overflow-x: auto;
                max-height: 500px;
            }}
        </style>
    </head>
    <body>
        <div class="block"><b>Name:</b> {name}</div>
        <div class="block"><b>user:</b> {username}</div>
        <div class="block"><b>Server Time (IST):</b> {time_ist}</div>
        <div class="block"><b>TOP output:</b></div>
        <div class="top-box">{top_output}</div>
    </body>
    </html>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
