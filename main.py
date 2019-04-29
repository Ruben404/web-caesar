from flask import Flask, render_template, flash, request
from caesar import rotate_string_13, alphabet_position


app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
        
            <label for="usertext">I want to encrypt:</label>
            <textarea name="usertext" type="text">{0}</textarea>
            by
            <textarea name="rot_val" type="text" value="0"></textarea>
            positions.
        
            <input type="submit" value="Submit">
            
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("","")

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form["usertext"]
    rotval = request.form["rot_val"]
    encrypted = rotate_string_13(text, rotval)
    print(encrypted)
    return form.format(encrypted)
app.run()