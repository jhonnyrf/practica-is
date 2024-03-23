from flask import Flask

app=Flask(__name__)

@app.route("/")  #decorador
def index():
    return "<h1>hola mundo<h1/>"