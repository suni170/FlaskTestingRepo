from flask import Flask, jsonify
from child_package.child_script import main  # Import function correctly

app = Flask(__name__)

@app.route('/parent')
def hello():
    return "hello world this is the testing new file"

@app.route('/')
def child():
    try:
        output = main()  # Calling function from child repo
        return jsonify({"message": "Child triggered", "output": output})
    except Exception as e:
        return jsonify({"error": "Error executing child script", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
