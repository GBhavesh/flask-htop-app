# Flask Htop App

A simple Flask-based web application that displays system information and running processes using the `top` command. Perfect for monitoring system status in real time.

## 📌 Features

- View server time in IST (Indian Standard Time)
- Get real-time system resource usage via `/htop` route
- Clean HTML output with monospace styling
- Built using Python + Flask

## 🚀 Live Demo

You can access the app at:
http://localhost:5000/htop

_(If hosted publicly, replace the above URL with the actual deployed URL)_

## 🛠️ Tech Stack

- Python 3
- Flask
- `subprocess` (to execute system commands)
- `pytz` (for timezone handling)

## 📁 Folder Structure
lask-htop-app/ ├── app.py ├── README.md ├── requirements.txt └── ...

## 🔧 How to Run

1. Clone this repository:

```bash
git clone https://github.com/GBhavesh/flask-htop-app.git
cd flask-htop-app
Install dependencies:

bash

pip install -r requirements.txt
Run the Flask app:

bash

python app.py
Visit in browser:

bash

http://localhost:5000/
http://localhost:5000/htop






