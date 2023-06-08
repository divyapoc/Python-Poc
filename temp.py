from flask import Flask,render_template

temp = Flask(__name__)
@temp.route('/')
def func():
    return render_template('app.html', name='Divya', rainy=True)

if __name__ == '__main__':
    temp.run()