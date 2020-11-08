from flask import Flask
from flask import render_template, request
from helper import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    searchKey = request.args['key']
    diction = top_headlines_search(searchKey)
    return render_template('news.html', header=searchKey, news=diction)



@app.route('/category', methods=['GET'])
def category():
    cntry = "in"
    category_request = request.args['category']
    diction = get_top_headlines_category(category_request)
    return render_template('news.html', category=category, news=diction)


@app.route('/source', methods=['GET'])
def source():
    src = request.args['source']
    diction = get_news_from_source(src)
    return render_template('news.html', category=source, news=diction)


@app.route("/country", methods=['GET'])
def country():
    cntry = request.args['source']
    diction = get_top_headlines_country(cntry)
    return render_template('news.html', news=diction)


if __name__ == '__main__':
    app.run(debug=True)
