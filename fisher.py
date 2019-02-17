import json
from flask import Flask, make_response, jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q :普通关键字 isbn
        page
    """
    # isbn isbn13 由13个0-9的数字组成
    # isbn10 10个数字组成，含有一些'-'
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}


# app.add_url_rule('/hello',view_func=hello)

app.run(host='0.0.0.0', debug=app.config['DEBUG'])
