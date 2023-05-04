import json
import random
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def hello():
    # Read the value of the 'username' cookie, or use a default value if it doesn't exist
    username = request.cookies.get('username', 'Guest')

    # Generate a random number between 1 and 10
    number = random.randint(1, 10)

    # Create a dictionary to represent the response data
    data = {'username': username, 'number': number}

    # Serialize the data as JSON
    json_data = json.dumps(data)

    # Create a response with the JSON data and set the 'username' cookie
    resp = make_response(json_data)
    resp.set_cookie('username', 'John')

    return resp

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

