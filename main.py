import os
import sys
import imgbank
import sqlite3
import random
from flask import Flask, render_template, request, g, session, redirect, url_for

reactionbank = Flask(__name__)


#Home page
@reactionbank.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        request.files["image"].save(str(random.randint(1000, 9999)) + ".png")
    return render_template('index.html')

if __name__ == "__main__":
    reactionbank.run(ssl_context="adhoc")