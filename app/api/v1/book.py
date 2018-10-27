from sqlalchemy import or_
from flask import jsonify
from app.libs.redprint import RedPrint
from app.models.book import Book
from app.validators.forms import BookSearchValidator

api = RedPrint('book')


@api.route('/search', methods=['GET'])
def search():
    form = BookSearchValidator().validate_for_api()
    q = '%' + form.q.data + '%'
    books = Book.query.filter_by(or_(Book.title.like(q), Book.pubdate(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)


@api.route('<isbn>/detail', methods=['GET'])
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)


