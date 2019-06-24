#!/usr/bin/env python
#
# Created on June, 2019
# @author: Katie Gamanji (gamanjie@gmail.com)
# All rights reserved 

from flask import jsonify
from flask import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify(
        taski_owner="Kiwi.com",
        challenge="Cloud challenge",
        user="Katie Gamanji"
    )

@app.route('/healthcheck')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
