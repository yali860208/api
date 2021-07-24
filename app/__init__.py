# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
from app import model
import json

app = Flask(__name__)
CORS(app)

@app.route('/cost', methods=['POST'])
def usageaccountid_to_unblendedcost():
    input_id = request.get_json()
    result = model.sum_unblendedcost(int(input_id['uid_cost']))
    return result

@app.route('/amount', methods=['POST'])
def usageaccountid_to_usageamount():
    input_id = request.get_json()
    result = model.sum_usageamount(int(input_id['uid_amount']))
    return result

@app.route('/uid', methods=['POST'])
def list_usageaccountid():
    input_id = request.get_json()
    result = model.list_uid(int(input_id['pid_uid']))
    return result

@app.route('/count', methods=['POST'])
def usageaccountid_to_usagecount():
    input_id = request.get_json()
    result = model.sum_usagecount(int(input_id['uid_count']))
    return result


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='127.0.0.1', port=port)