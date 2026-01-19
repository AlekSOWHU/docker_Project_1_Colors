from flask import Flask, render_template, request, jsonify
import os
import datetime

app = Flask(__name__)

# Define where we will save the file inside the container
DATA_FILE = '/app/data/clicks.txt'

# Ensure the directory exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def click():
    data = request.json
    color = data.get('color', 'unknown')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append the click to the text file
    with open(DATA_FILE, 'a') as f:
        f.write(f"Color clicked: {color} at {timestamp}\n")
    
    print(f"Logged: {color}", flush=True)
    return jsonify({"status": "success", "color": color})

if __name__ == '__main__':
    # Host='0.0.0.0' is crucial to make the server accessible outside the container
    app.run(host='0.0.0.0', port=5000)