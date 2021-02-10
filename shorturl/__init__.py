from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mvugcvrknffrvq:17c7a430ef41c94c41563db7e1af426d8d80665474109ed7dff8d20c0d097ff1@ec2-54-237-155-151.compute-1.amazonaws.com:5432/ddoq86oomosaln'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from shorturl import main
