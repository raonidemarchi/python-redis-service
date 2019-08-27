from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
  return {
    'hello': 'world'
  }

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')