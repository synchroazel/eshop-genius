from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from sqlalchemy import exc

from eshop_handlers import search_game
from webapp import db
from .models import User
from .models import Wishlist

search = Blueprint('search', __name__)


@search.route('/search', methods=['GET', 'POST'])
def search_page():
    user = User.query.filter_by(username=None).first()

    if request.method == 'POST':

        query = request.form.get('query')

        global results
        results = search_game(query)  # the actual search

        return redirect(url_for('search.results_page'))
    return render_template('search.html', user=current_user)


@search.route('/results', methods=['GET', 'POST'])
def results_page():
    if request.method == 'POST':

        chosen_game_id = request.form["chosen_game"]

        print(f'\n\n[DEBUG] You clicked on game {chosen_game_id}\n\n')

        try:
            new_wishlist = Wishlist(content=chosen_game_id, user_id=current_user.id)
            db.session.add(new_wishlist)
            db.session.commit()
            flash('Game successfully added to your wishlist!', category='success')
        except exc.IntegrityError:
            flash('Game already in your wishlist!', category='error')

    query = request.form.get('query')

    global results
    results = search_game(query)  # the actual search

    return render_template('results.html', results=results, user=current_user)
