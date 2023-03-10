from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Bowling.db" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "segreto"

db = SQLAlchemy(app)
from models import models
app.app_context().push()
db.create_all()
  





@app.route("/")
def hello():
  return "Hello World!"


@app.route("/ping")
def pong():
    return "pong"
    
if __name__ == "__main__":
  app.run(debug=True)