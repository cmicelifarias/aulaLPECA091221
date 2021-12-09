from flask import Flask

app = Flask(__name__)

#decorator -> decorador
@app.route("/")
def hello():
    return "<h1>Oi Mundo!</h1>"

app.run()