from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def formPage():
    return render_template('page.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
