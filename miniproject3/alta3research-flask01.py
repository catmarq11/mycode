#!/usr/bin/env python3
""""""

import json
import random
import datetime
from flask import Flask, render_template, make_response

app = Flask(__name__)

with open("dadJokes.json", "r") as file:
      data= json.load(file)

@app.route('/data')
def get_data():
    return data

@app.route('/', methods=['GET'])
def home():
   return render_template('home.html')

@app.route('/jokes')
def get_some_jokes():
    return data
   # return {"Date" : datetime.today()} #returns date/time in JSON

@app.route('/jokes/random')
def random_joke():
   randomJoke = random.choice(data["jokes"])
   return render_template('home.html', setup=randomJoke['setup'], punchline=randomJoke['punchline'])


@app.route('/setcookie')
def setcookie():
  expires = datetime.datetime.now() + datetime.timedelta(hours=1)
  domain = 'example.com'
  path = '/'
  secure = True
  httponly = True
  resp = make_response('Setting Restricted Cookie for security!')
  resp.set_cookie('username', 'Cat', expires=expires, domain=domain, path=path, secure=secure, httponly=httponly)
  return resp




if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=2224) # runs the application
