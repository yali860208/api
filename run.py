# -*- coding: UTF-8 -*-
from app import app

@app.route('/')
def index():
    return 'Flask API started'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)