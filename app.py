from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from initialize import *

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from route import *

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
