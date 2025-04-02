#_____Imports_____
from flask import Flask, render_template, request, session, url_for
import json
import Drinks #functions containing the instructions and images for each drink

app = Flask(__name__)

@app.route('/', methods=['GET', 'Post'])
def HomePage():
    if request.method == 'POST':
        session['button_value'] = request.form.get('button_value') #stores button value so that it can be retreved elsewhere
    return render_template('HomePage.html')

@app.route('/Preparing', methods=['GET', 'Post'])
def Preparing():
    instructions = ["No instructions Found"]
    button_value = request.form.get('button_value') or session.get('button_value')
    match button_value: #match case works like a set of if and elif statements
        case "LemonTea":
            instructions = Drinks.LemonTea_Text()
            images = [url_for('static', filename=f'Images/{img}') for img in Drinks.LemonTea_Images()]
        
        case "HotChocolate":
            instructions = Drinks.HotChocolate()
            images = [url_for('static', filename=f'Images/{img}') for img in Drinks.HotChocolate_Images()]
    
        case "Coffee":
            return render_template('Coffees.html')
    
        case "Home":
            return render_template('HomePage.html')
        
        case "Coffee_Americano":
            instructions = Drinks.Coffee_Americano()
            images = [url_for('static', filename=f'Images/{img}') for img in Drinks.Coffee_Americano_Images()]
        
        case "Coffee_Latte":
            instructions = Drinks.Coffee_Latte()
            images = [url_for('static', filename=f'Images/{img}') for img in Drinks.Coffee_Latte_images()]

    return render_template('TextPage.html', Text = "...", instructionarray = json.dumps(instructions), imagearray = json.dumps(images)) #coverts the array to JSON so that it can be used with Javasript in the HTML files
    



