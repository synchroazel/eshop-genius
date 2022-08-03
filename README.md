# eShop genius

A simple webapp to keep track of your Nintendo Switch games wishlist. Create an account in 5 seconds with a username and
a password and start adding your favorite games right away!

The webapp is available [here](https://eshop-genius.herokuapp.com)*!*

## How does it work?

The webapp is completely made with Python and Flask. It uses a SQLite database to store accounts and wishlists and it's
hosted to Heroku. To search games on the eShop and their info, the [Nintendeals](https://pypi.org/project/nintendeals/)
libraries were used.

## Limitations

The webapp currently shows only deals on the european eShop, with prices in EUR. Possibility to switch country/zone
and currency might come soon.
