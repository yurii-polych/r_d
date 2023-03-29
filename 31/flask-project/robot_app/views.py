from robot_app import app


@app.route('/hello')
def greeting():
    app.logger.info(r'Logging info "\hello."')
    return 'Hello, world!'
