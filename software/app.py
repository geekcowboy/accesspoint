from flask import Flask, request, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from sandman import app as sandman_app
from sandman.model import activate, register, Model
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from werkzeug.debug import DebuggedApplication

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getcwd() + '/venv/test.db'
app.debug = True
db = SQLAlchemy(app)

sandman_app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
sandman_app.debug = True


class RfidKey(db.Model):
  id = db.Column(db.Integer, primary_key=True,nullable=False)
  rfidKey = db.Column(db.String(80))
  
  def __init__(self, rfidKey):
    self.rfidKey = rfidKey
        
  def __repr__(self):
    return '<Rfid %r>' % self.rfidKey

class RfidKeyApi(Model):
  __tablename__ = "rfid_key"
  __endpoint__ = "rfids"

@app.route('/')
def index():
  return "Hello World"

if __name__ == "__main__":

  register(RfidKeyApi)
  activate(browser=False)

  application = DispatcherMiddleware(app, {
    '/api': sandman_app,
    })

  debugged_app = DebuggedApplication(application, evalex=True)
    
  run_simple('0.0.0.0', 8080, debugged_app, use_reloader=True, use_debugger=True, use_evalex=True)
