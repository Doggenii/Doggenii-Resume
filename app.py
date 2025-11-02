from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.HTML')
"""
@app.route('/')
def ():
    return
next function for page
"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)