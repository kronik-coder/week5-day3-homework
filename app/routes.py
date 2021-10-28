from flask import render_template, request
import requests
from app import app
from .forms import EnterPokemonForm, LoginForm, RegisterForm

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = EnterPokemonForm()
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        pokemon = response.json()
        if response.ok:
            stats = {
                "name": pokemon["forms"][0]["name"],
                "hp": pokemon["stats"][0]["base_stat"]  ,
                "defense": pokemon["stats"][2]["base_stat"],
                "attack": pokemon["stats"][1]["base_stat"],
                "shiny": pokemon["sprites"]["front_shiny"]
                }
            return render_template('search.html.j2', stats=stats, form=form)
    return render_template('search.html.j2', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template('login.html.j2', form=form)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    new_user_data = {
        "first_name": form.first_name.data,
        "last_name": form.last_name.data,
        "email": form.email.data,
        "password": form.password.data
    }

    return render_template('registration.html.j2', form=form)

# python -m venv venv
# Windows: venv\scripts\activate
# If the requirements.txt has pkg-resources == 0.0.0 inside of it delete this line and press save (this is something that only works with linux)
# pip install -r requirements.txt
# windows: set FLASK_APP=app,py
# windows: set FLASK_ENV=development
# flask run

# pip install python-dotenv