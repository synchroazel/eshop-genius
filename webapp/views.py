from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from eshop_handlers import get_game_info

from webapp import db
from .models import Wishlist

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        id_to_remove = request.form["remove_game"]

        Wishlist.query.filter_by(content=id_to_remove, user_id=current_user.id).delete()
        db.session.commit()
        flash('Game successfully removed from your wishlist!', category='error')

    user_wishlist = Wishlist.query.filter_by(user_id=current_user.id).all()

    payload = list()

    for game in user_wishlist:
        info = get_game_info(game.content)
        payload.append(info)

    return render_template("home.html", user=current_user, payload=payload)
