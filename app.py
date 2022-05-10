from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def codesp():
    return render_template("index.html", title= 'ProjectsPy')
app.run(host='0.0.0.0', port=5000)

