import os
from robot_app import app, db
from flask import jsonify, request
from .models import User, Purchase, Book


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def get_size_from_params():
    size = None
    if 'size' in request.args.keys():
        size = int(request.args.get('size'))
    return size


def get_rows_from_model(model):
    size = get_size_from_params()
    if size:
        rows = db.session.scalars(db.Select(model).limit(size))
        return rows
    else:
        rows = db.session.scalars(db.Select(model))
        return rows


@app.post('/users')
def add_user():
    user = User(
        first_name=request.form.get('first_name'),
        last_name=request.form.get('last_name'),
        age=request.form.get('age')
    )
    db.session.add(user)
    db.session.commit()
    return 'User added.'


@app.route('/users')
def get_users():
    users = get_rows_from_model(User)
    result = [{
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age
        } for user in users]
    return jsonify(result)


@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = db.get_or_404(User, user_id)
    result = [{
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age
        }]
    return jsonify(result)


@app.post('/books')
def add_book():
    book = Book(
        title=request.form.get('title'),
        author=request.form.get('author'),
        year=request.form.get('year'),
        price=request.form.get('price')
    )
    db.session.add(book)
    db.session.commit()
    return 'Book added.'


@app.route('/books')
def get_books():
    books = get_rows_from_model(Book)

    result = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price
        } for book in books]
    return jsonify(result)


@app.route('/books/<int:book_id>')
def get_book_by_id(book_id):
    book = db.get_or_404(Book, book_id)
    result = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price
        }]
    return jsonify(result)


@app.post('/purchases')
def add_parchase():
    try:
        user_id = request.form.get('user_id')
        book_id = request.form.get('book_id')
        if db.get_or_404(User, user_id) and db.get_or_404(Book, book_id):
            purchase = Purchase(
                user_id=user_id,
                book_id=book_id,
            )
            db.session.add(purchase)
            db.session.commit()
            return 'Purchase added.'
    except Exception:
        return f"There is not user_id: {user_id} or book_id: {book_id}."


@app.route('/purchases')
def get_purchases():
    purchases = get_rows_from_model(Purchase)
    result = [{
        'id': purchase.id,
        'user_id': purchase.user_id,
        'book_id': purchase.book_id,
        'date': purchase.date,
        'book title': purchase.book.title,
        'user_name': purchase.user.first_name
    } for purchase in purchases]
    return jsonify(result)


@app.route('/purchases/<int:purchase_id>')
def get_purchases_by_id(purchase_id):
    purchase = db.get_or_404(Purchase, purchase_id)
    result = [{
        'id': purchase.id,
        'user_id': purchase.user_id,
        'book_id': purchase.book_id,
        'date': purchase.date,
        'book title': purchase.book.title,
        'user_name': purchase.user.first_name
    }]
    return jsonify(result)
