from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class RFIDKey(db.Model):
  id = db.Column(db.Integer, primary_key=True,nullable=False)
  rfidKey = db.Column(db.String(80))
  
  def __init__(self, rfidKey):
    self.rfidKey = rfidKey
        
  def __repr__(self):
    return '<Rfid %r>' % self.rfidKey