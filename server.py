import os
from flask import (Flask, render_template, request, 
                   redirect, session, flash, jsonify,
                   Markup)
from model import connect_to_db


app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']







if __name__ == '__main__':
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run()