# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
from app import model

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['POST'])
def test_cost():
    # 取得前端傳過來的數值
    input_id = request.get_json()
    result = model.sum_unblendedcost(959256351448)
    return result

@app.route('/predict', methods=['POST'])
def predict_cost_amount():
    # 取得前端傳過來的數值
    input_id = request.get_json()
    output_id = {}
    cost = model.sum_unblendedcost(int(input_id['uid_cost']))
    amount = model.sum_usageamount(int(input_id['uid_amount']))
    output_id['unblendedcost'] = cost
    output_id['usageamount'] = amount
    return output_id

@app.route('/cost', methods=['POST'])
def usageaccountid_to_unblendedcost():
    # 取得前端傳過來的數值
    input_id = request.get_json()
    result = model.sum_unblendedcost(int(input_id['uid_cost']))
    return result

@app.route('/amount', methods=['POST'])
def usageaccountid_to_usageamount():
    # 取得前端傳過來的數值
    input_id = request.get_json()
    result = model.sum_usageamount(int(input_id['uid_amount']))
    return result


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)