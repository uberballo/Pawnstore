from flask import Flask, render_template
from application import app

@app.route("/")
def hello():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
