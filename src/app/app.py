from distutils.log import debug
from database.select import Select
from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    select = Select()
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        request_data = request.json
        method = request_data.get("method","")
        query = request_data.get("query","")
        if method != "ein" and method != "name":
            return 'Parameter "method" needs to be equal to name or ein',400
        if not query:
            return 'Invalid query',400
        
        if method == "ein":
            return {"result":select.select_data_by_ein(query)}
        else:
            return {"result":select.select_data_by_name(query)}
        
    else:
        return 'Content-Type not supported!',400


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)