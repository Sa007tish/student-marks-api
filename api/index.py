from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Student data directly in the code
student_data = {
    "Z": 90,
    "QmO": 91,
    "s0t6lf8": 98,
    "lc3E1QHtgz": 98,
    "5PzomMY5": 95
    # Add more students as needed
}

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
