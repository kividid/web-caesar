from flask import Flask, request
from caesar import encrypt

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
        <form action="/" method="POST">
            <label for="rotate">Rotate By:</label>
            <input type="text" name="rot" id="rotate" value="0">
            <textarea name="text" id="" cols="30" rows="10">{0}</textarea>
            <input type="submit" value="Encode">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def cypher():
    text = request.form['text']
    rot = request.form['rot']
    rot = int(rot)

    return form.format(encrypt(text, rot))



app.run()