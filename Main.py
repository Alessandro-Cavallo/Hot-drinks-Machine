#launching UI and calling drinks
#_____Imports_____
from time import sleep
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'Post'])
def HomePage():
    global button_value
    button_value = None
    if request.method == 'POST':
        button_value = request.form.get('button_value')
    return render_template('HomePage.html')

@app.route('/Preparing')
def Preparing():
    return render_template('TextPage.html', Text = button_value)



