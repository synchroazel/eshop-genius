from datetime import datetime

from babel import numbers
from nintendeals import noe
from nintendeals.api import prices


def search_game(query):
    response = noe.search_switch_games(query)

    query = query.split()

    for i in range(len(query)):
        query[i] = ''.join(char.lower() for char in query[i] if char.isalnum())

    results = dict()

    for game in response:

        original_title = game.title
        game_id = game.nsuid
        game_title = game.title.split()

        for i in range(len(game_title)):
            game_title[i] = ''.join(char.lower() for char in game_title[i] if char.isalnum())

        matched_words = len(set(query) & set(game_title))

        results[(original_title, game_id)] = matched_words

    best_results = sorted(results, key=results.get, reverse=True)[:10]

    return best_results


def get_game_info(game_id, country='IT'):
    game = noe.game_info(game_id)
    price = prices.get_price(game, country=country)

    in_sale = False if price.sale_discount == 0 else True

    current_price = price.sale_value if in_sale else price

    if price.sale_start != None:
        sale_start = price.sale_start.strftime("%d/%m")
        sale_end = price.sale_end.strftime("%d/%m")
        daysleft = (price.sale_end - datetime.now()).days
    else:
        sale_start, sale_end, daysleft = None, None, None

    return {'title': game.title,
            'game_id': game_id,
            'in_sale': in_sale,
            'current_price': f'{current_price}{numbers.get_currency_symbol(price.currency)}',
            'price': f'{price.value}{numbers.get_currency_symbol(price.currency)}',
            'discount': f'{100 - price.sale_discount}%',
            'sale_start': sale_start,
            'sale_end': sale_end,
            'daysleft': daysleft,
            'link': game.eshop.it_it
            }
