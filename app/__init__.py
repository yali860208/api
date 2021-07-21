# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/cost', methods=['POST'])
def usageaccountid_to_unblendedcost():
    # 取得前端傳過來的數值
    input_id = request.get_json()
    result = model.sum_unblendedcost(input_id['uid_count'])
    return result

@app.route('/amount', methods=['POST'])
def usageaccountid_to_usageamount():
    # 取得前端傳過來的數值
    input_id = request.get_json()
    result = model.sum_usageamount(input_id['uid_amount'])
    return result


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)