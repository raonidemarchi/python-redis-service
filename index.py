from flask import Flask, request, jsonify
import redis
import sys
import random

app = Flask(__name__)
redis = redis.Redis('redis')

redis.set('last-request', 'teste')

@app.route('/<username>/<password>')
def hello(username, password):
  redis.set('username', username)
  redis.set('token', random.randint(20000, 1000000))

  return {
    'hello': 'foi'
  }

@app.route('/validateAuth')
def hello2():
  result = 'Not Authenticated' if redis.get('username') == None else redis.get('token').decode('utf-8')

  return {
    'result': result
  }

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')