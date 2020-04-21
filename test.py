from flask import Flask, render_template, flash, request, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from register import *
from movie import *
from recommender_system import *

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

app.register_blueprint(register_api)
app.register_blueprint(movie_api)
app.register_blueprint(recommend_api)

@app.route('/')
def index():
    query = "MATCH (m:Movie) RETURN m.movie_title"
    movies = db.neo4j_driver.session().run(query).values()
    movies = [movie[0] for movie in movies]

    return render_template("index.html", movies = movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
