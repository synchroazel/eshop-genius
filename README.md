# eShop genius

A simple webapp to keep track of your Nintendo Switch games wishlist. Available [here](https://eshop-genius.herokuapp.com)*!*

## How does it work?

The webapp is completely made with Python and Flask. It uses a SQLite database to store accounts and wishlists and it's
hosted to Heroku. To search games on the eShop and their info, the [Nintendeals](https://pypi.org/project/nintendeals/)
library was used.

## Limitations

The webapp currently shows only deals on the european eShop, with prices in EUR. Possibility to switch country/zone
and currency might be added later.
