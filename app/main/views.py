from . import main
from flask import render_template
from app.requests import get_items

@main.route('/')
def index():
    name = get_items()
    return render_template('index.html', name = name)
