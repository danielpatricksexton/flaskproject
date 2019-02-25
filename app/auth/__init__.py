from flask import Blueprint

auth = Blueprint('auth', __name__)

from app.auth import routes


# Blueprint is a class that we are importing

# now we instantiate auth
