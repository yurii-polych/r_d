import os
from robot_app import app
from random import randint, sample
from flask import request, redirect, abort, render_template, session, url_for
from re import fullmatch


app.secret_key = os.getenv('SECRET_KEY')


@app.route('/hello')
def greeting():
    app.logger.info(r'Logging info "\hello."')
    return 'Hello, world!'


# Task 32.1, 32.7, 33.1, 33.3. =========================================================
def get_count_amount_from_params():
    count_amount = None
    if 'count' in request.args.keys():
        count_amount = int(request.args.get('count'))
    return count_amount


@app.route('/users')
def get_users():
    if 'user' not in session:
        return redirect('/login')

    names = ['Herman', 'Gabriel', 'Miguel', 'James', 'Marcel']
    names_len = len(names)

    users_amount = get_count_amount_from_params()

    if not users_amount:
        random_amount = randint(1, names_len)
        result = sample(names, k=random_amount)
        return get_html_list(result)
    elif users_amount >= names_len:
        return get_html_list(names)
    else:
        return get_html_list(sample(names, k=users_amount))


def get_html_list(things_list):
    return render_template('html_list.html', attrs=things_list, username=session['user'])


@app.route('/books')
def get_books():
    if 'user' not in session:
        return redirect('/login')

    books = ['In Search of Lost Time', 'Ulysses', 'Don Quixote', 'The Great Gatsby', 'Moby Dick']
    books_len = len(books)

    books_amount = get_count_amount_from_params()

    if not books_amount:
        random_amount = randint(1, books_len)
        random_books = sample(books, k=random_amount)
        return get_html_list(random_books)
    elif books_amount >= books_len:
        return get_html_list(books)
    else:
        return get_html_list(sample(books, k=books_amount))


# Task 32.2, 33.1, 33.3. =========================================================
@app.get('/users/<int:user_id>')
def get_user_id(user_id):
    if 'user' not in session:
        return redirect('/login')

    if not user_id % 2:
        return render_template('user_id.html', id=user_id, username=session['user'])
    return abort(404)


@app.get('/books/<string:title>')
def get_book_title(title):
    if 'user' not in session:
        return redirect('/login')

    title_capitalize = title.capitalize()
    return render_template('books_title.html', book_title=title_capitalize, username=session['user'])


# Task 32.3, 33.1, 33.3. =========================================================
@app.get('/params')
def get_parameters_html_table():
    if 'user' not in session:
        return redirect('/login')

    return render_template('params.html', username=session['user'], attrs=request.args.to_dict())


# Task 32.4, 32.8, 33.1, 33.2, 33.3 =========================================================
def validate_password(psw):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    return fullmatch(pattern, psw)


def validate_username(name):
    return len(name) >= 5


@app.route('/login', methods=['GET', 'POST'])
def get_html_form():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        request_data = request.form.to_dict()
        username = request_data.get('user')
        password = request_data.get('password')

        if username and password and validate_username(username) and validate_password(password):
            session['user'] = username
            return redirect('/users'), 301
        else:
            abort(400, 'The username/password are missing or username/password are invalid.')


# Task 32.5. =========================================================
@app.errorhandler(404)
def handle_error_404(e):
    return f'<div>Sorry, file not found.</div>', 404


@app.errorhandler(500)
def handle_error_500():
    return '<div>Oooops, there is an internal server error.</div>', 500


# Task 32.6, 33.1, 33.3. =========================================================
@app.route('/')
def get_url_pages():
    if 'user' not in session:
        return redirect('/login')

    url = request.url
    pages = ['/login', '/users', '/books', '/params']
    pages_dict = {}
    for page in pages:
        pages_dict[page] = url + page
    return render_template('urls_page.html', username=session['user'], attrs=pages_dict)


# Task 33.4.
@app.post('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')
