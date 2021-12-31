from flask import Flask
from apiflask import APIFlask
app = APIFlask(__name__)
import bilal_backend.views

