from flask import Blueprint

api = Blueprint('api',__name__)

from . import api_hello 
from .auth import registerApi