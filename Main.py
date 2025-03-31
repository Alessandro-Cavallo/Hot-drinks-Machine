#_____Imports_____
from time import sleep
from flask import Flask, render_template, request, session, url_for
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
    instructions = ["No instructions Found"]
    button_value = request.form.get('button_value') or session.get('button_value')
    print(f"Button Value: {button_value}")#debug
    if button_value == "LemonTea":
        instructions = Drinks.LemonTea_Text()
        images = [url_for('static', filename=f'Images/{img}') for img in Drinks.LemonTea_Images()]
        print(f"Instructions: {instructions}") #debug
        
    elif button_value == "HotChocolate":
        instructions = Drinks.HotChocolate()
        images = [url_for('static', filename=f'Images/{img}') for img in Drinks.HotChocolate_Images()]
    
    elif button_value == "Coffee":
        return render_template('Coffees.html')
    
    elif button_value == "Coffee_Americano":
        instructions = Drinks.Coffee_Americano()
        images = [url_for('static', filename=f'Images/{img}') for img in Drinks.Coffee_Americano_Images()]

    return render_template('TextPage.html', Text = "...", instructionarray = json.dumps(instructions), imagearray = json.dumps(images)) #coverts the array to JSON so that it can be used with Javasript in the HTML files
    



