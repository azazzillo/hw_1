from flask.app import Flask as FlaskApp
from flask import Flask
import requests

response = requests.get(
    'https://api.hearthstonejson.com'
    '/v1/121569/ruRU/cards.collectible.json')

cards: list[dict] = response.json()

app: Flask = Flask(__name__)

@app.route('/g')
def card_s():
    return cards

if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    )
