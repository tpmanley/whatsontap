from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text


__version__ = "0.1"

app = Flask(__name__, static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tap.db'
db = SQLAlchemy(app)


class Tap(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=False)
    style = Column(Text, unique=False)
    abv = Column(Text, unique=False)
    description = Column(Text, unique=False)
    image = Column(Text, unique=False)


api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Tap, methods=['GET', 'POST'])


@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run()

