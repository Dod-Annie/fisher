from flask import Flask, make_response
from helper import is_isbn_or_key

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
    isbn_or_ky = is_isbn_or_key(q)
    pass


# app.add_url_rule('/hello',view_func=hello)

app.run(host='0.0.0.0', debug=app.config['DEBUG'])
