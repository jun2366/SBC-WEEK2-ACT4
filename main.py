from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)