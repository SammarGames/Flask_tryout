from flask import Flask  

app = Flask(__name__)  

@app.route('/')  
def hello_world():
    return "<p>Les 11 huiswerk opdracht, kijken of meneer Declerck het goed vind :)</p>"  