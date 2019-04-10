from flask import Flask, render_template, flash, request


app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/encrypt" methon="post">
        <label>
            I want to encrypt 
            <input type="text" name="rot"/>
            .
        </label>
        <input type="submit" value="0"
    </body>
</html>
"""

@app.route("/")
def index():
    return form