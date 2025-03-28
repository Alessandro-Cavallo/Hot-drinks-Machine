#_____Imports_____
from time import sleep
from flask import Flask, render_template, request, session
import json
import Drinks #functions containing the instructions for each drink

app = Flask(__name__)

@app.route('/', methods=['GET', 'Post'])
def HomePage():
    if request.method == 'POST':
        session['button_value'] = request.form.get('button_value') #stores button value so that it can be retreved elsewhere
        print(f"Button Value: {session.get('button_value')}")#debug
    return render_template('HomePage.html')

@app.route('/Preparing', methods=['GET', 'Post'])
def Preparing():
    button_value = request.form.get('button_value') or session.get('button_value')
    print(f"Button Value: {button_value}")#debug
    if button_value == "LemonTea":
        instructions = Drinks.LemonTea()
        print(f"Instructions: {instructions}") #debug
    return render_template('TextPage.html', Text = "...", instructionarray = json.dumps(instructions)) #coverts the array to JSON so that it can be used with Javasript in the HTML files


