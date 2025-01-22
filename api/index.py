from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def load_student_data():
    try:
        # Get absolute path to the JSON file
        current_dir = os.path.dirname(os.path.realpath(__file__))
        json_path = os.path.join(current_dir, 'q-vercel-python.json')
        
        with open(json_path, 'r') as f:
            data = json.load(f)
            # Convert list of dicts to a simple name:marks dict
            return {item['name']: item['marks'] for item in data}
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return {}

# Load data when the module initializes
student_data = load_student_data()

@app.route('/api', methods=['GET'])
def get_marks():
    try:
        names = request.args.getlist('name')
        marks = []
        
        for name in names:
            if name in student_data:
                marks.append(student_data[name])
        
        return jsonify({"marks": marks})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "API is running. Use /api?name=X&name=Y to get marks."

if __name__ == '__main__':
    app.run()
