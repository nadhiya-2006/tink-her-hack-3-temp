from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

# File to store data
DATA_FILE = "data.json"

# Function to read data from the file
def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

# Function to write data to the file
def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    # Read data from the file
    data = read_data()
    semester2_data = data.get('semester2', [])
    
    return render_template('index.html', semester2_data=semester2_data)

@app.route('/add-semester2', methods=['POST'])
def add_semester2():
    # Read the existing data
    data = read_data()

    # Get new data from the form
    new_course = request.form['course']
    
    # If no data exists for 'semester2', create an empty list
    if 'semester2' not in data:
        data['semester2'] = []
    
    # Add the new course to the semester2 data
    data['semester2'].append(new_course)

    # Save the updated data back to the file
    write_data(data)

    return jsonify({"message": "Course added successfully!", "new_course": new_course})

if __name__ == '__main__':
    app.run(debug=True)
