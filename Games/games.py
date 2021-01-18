import json
from sqlite3.dbapi2 import connect
import ssl
import urllib.request
import sqlite3


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = sqlite3.connect('games.db')
cur = connection.cursor()
cur.execute('DROP TABLE IF EXISTS Games')
cur.execute('''CREATE TABLE IF NOT EXISTS Games(id TEXT, title TEXT, thumbnail TEXT, short_description TEXT, game_url TEXT, genre TEXT,
            platform TEXT, publisher TEXT, developer TEXT, release_date TEXT);''')

endpoint = 'https://www.freetogame.com/api/games'
url_data = urllib.request.urlopen(endpoint, context=ctx)
data = url_data.read().decode()

json_data = json.loads(data)
js_dump = json.dumps(json_data, indent=4)
print (js_dump)


for game in json_data:
    id = game['id']
    title = game['title']
    thumbnail = game['thumbnail']
    short_description = game['short_description']
    game_url = game['game_url']
    genre = game['genre']
    platform = game['platform']
    publisher = game['publisher']
    developer = game['developer']
    release_date = game['release_date']

    cur.execute('INSERT INTO Games VALUES (?,?,?,?,?,?,?,?,?,?)', (id, title, thumbnail, short_description, game_url, genre,
    platform, publisher, developer, release_date,))
connection.commit()





#id, title, thumbnail, short_description, game_url, genre,
     #       platform, publisher, developer, release_date, freetogame_profile
