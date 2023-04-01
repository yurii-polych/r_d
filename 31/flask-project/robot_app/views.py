from robot_app import app
from random import randint, sample
from flask import request, redirect, abort
from re import fullmatch


@app.route('/hello')
def greeting():
    app.logger.info(r'Logging info "\hello."')
    return 'Hello, world!'


# Task 1, 7. =========================================================
def get_count_amount_from_params():
    count_amount = None
    if 'count' in request.args.keys():
        count_amount = int(request.args.get('count'))
    return count_amount


@app.route('/users')
def get_users():
    names = ['Herman', 'Gabriel', 'Miguel', 'James', 'Marcel']
    names_len = len(names)

    users_amount = get_count_amount_from_params()

    if not users_amount:
        random_amount = randint(1, names_len)
        result = sample(names, k=random_amount)
        return result
    elif users_amount >= names_len:
        return names
    else:
        return sample(names, k=users_amount)


def get_html_list(things_list):
    html_list = ''
    for thing in things_list:
        html_list += f'<li>{thing}</li>'
    return html_list


@app.route('/books')
def get_books():
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


# Task 2. =========================================================
@app.get('/users/<int:user_id>')
def get_user_id(user_id):
    if not user_id % 2:
        return f'<div>The user_id is: {user_id}.</div>'
    return '<div>Not Found</div>', 404


@app.get('/books/<string:title>')
def get_book_title(title):
    title_capatalize = title.capitalize()
    return f'<div>The book title is: {title_capatalize}.</div>'


# Task 3. =========================================================
@app.get('/params')
def get_parameters_html_table():
    params = request.args.to_dict()
    html_table = '<table><tr><th>parameter</th><th>value</th></tr>'
    for key, value in params.items():
        html_table += f'<tr><td>{key}</td><td>{value}</td></tr>'

    html_table += '</table>'
    return f'<div>{html_table}</div>'


# Task 4, 8. =========================================================
def validate_password(psw):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
    return fullmatch(pattern, psw)


def validate_username(name):
    return len(name) >= 5


@app.route('/login', methods=['GET', 'POST'])
def get_html_form():
    if request.method == 'GET':
        html_form = """
            <form action="/login" method="post">
            <label for="login-id">Username</label>
            <input type="text" name="username" id="login-id">
            <label for="password-id">Password</label>
            <input type="password" name="password" id="password-id">
            <button type="submit">Submit</button>
            </form>
            """
        return html_form, 200
    elif request.method == 'POST':
        request_data = request.form.to_dict()
        username = request_data.get('username')
        password = request_data.get('password')
        if username and password and validate_username(username) and validate_password(password):
            return redirect('/users'), 301
        else:
            abort(400, 'The username/password are missing or username/password are invalid.')


# Task 5. =========================================================
@app.errorhandler(404)
def handle_error_404():
    return '<div>Sorry, file not found.</div>', 404


@app.errorhandler(500)
def handle_error_500():
    return '<div>Oooops, there is an internal server error.</div>', 500


# Task 6. =========================================================
@app.route('/')
def get_url_pages():
    url = request.url
    pages = ['/login', '/users', '/books', '/params']
    html_links = '<div>'
    for page in pages:
        html_links += f'<a href="{url + page}">{page}</a><br>'
    html_links += '</div>'
    return html_links

