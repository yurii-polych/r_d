import os
# from robot_app import app, db
from . import app, db
from random import randint, sample
from flask import request, redirect, abort, render_template, session, url_for, jsonify
from re import fullmatch
from .models import User, Purchase, Book


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

