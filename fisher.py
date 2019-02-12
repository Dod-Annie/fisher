from flask import  Flask, make_response

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    headers={
        'content-type':'text/plain',
        'location':'http://www.bing.com'
    }
    response = make_response('<html></html>')
    response.headers = headers
    return response
    # return 'Hello World'

# app.add_url_rule('/hello',view_func=hello)

app.run(host='0.0.0.0',debug=app.config['DEBUG'])