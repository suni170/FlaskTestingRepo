from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world this is the testing new file"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
