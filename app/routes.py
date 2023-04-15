from flask import render_template, request
from app import app
from forms import Pokemon_search, Signup
import requests

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/signup')
def signup():
    form = Signup()
    if request.method == 'POST':
         if form.validate():
              username = form.username.data
              email = form.email.data
              password = form.password.data
    return render_template('signup.html', form = form)

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/search', methods=["GET", "POST"])
def poke_search():
    form = Pokemon_search()
    if request.method == "POST":
        pokemon_name = form.pokemon_name.data
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
        response = requests.get(url)
        if not response.ok:
                return "Try again?"

        data = response.json()
        for pokemon in data:
            poke_dict={}
            poke_dict={
                    "poke_id": data['id'],
                    "name": data['name'].title(),
                    "ability":data['abilities'][0]["ability"]["name"],
                    "base experience":data['base_experience'],
                    "photo":data['sprites']['other']['home']["front_default"],
                    "attack base stat": data['stats'][1]['base_stat'],
                    "hp base stat":data['stats'][0]['base_stat'],
                    "defense stat":data['stats'][2]["base_stat"]}
        return poke_dict
    return render_template('search.html', form = form)