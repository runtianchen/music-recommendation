from flask import abort, redirect, url_for, Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    print('index')
    # return redirect(url_for('login'))


@app.route('/log')
def login():
    # abort(401)
    return render_template('login.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
