from flask import Flask, send_from_directory,render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='', static_folder='Jogo')



@app.route('/jogo')
def index():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('Jogo', path)


@app.route('/login')
def send_files(path):
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)