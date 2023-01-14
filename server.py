from flask import Flask, render_template

app = Flask(__name__,template_folder='templates/',static_folder='static/')

@app.route("/")
def home():
    return "<p>Home</p>"

@app.route("/peder")
def miro():
    return "<p>Miro, peder!</p>"

@app.route("/igrac")
def igrac():
    return render_template("index.html")

@app.route("/trener")
def trener():
    return render_template("index.html")

@app.route("/klub")
def klub():
    return render_template("index.html")

@app.route("/drzava")
def drzava():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host='0.0.0.0.', debug=True)
   

