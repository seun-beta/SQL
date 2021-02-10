import json
import ssl
import urllib.request
import sqlite3

# Ignore SSL certificate errors
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

connection = sqlite3.connect('db.sqlite3')
cur = connection.cursor()
cur.execute('DROP TABLE IF EXISTS Games')
cur.execute('''CREATE TABLE IF NOT EXISTS Games(id TEXT, title TEXT,
            thumbnail TEXT,short_description TEXT, game_url TEXT,
            genre TEXT,platform TEXT, publisher TEXT, developer TEXT, 
            release_date TEXT);''')

api_endpoint = 'https://www.freetogame.com/api/games'
response_data = urllib.request.urlopen(api_endpoint, context=context)
data = response_data.read().decode()
json_data = json.loads(data)
#json_dump = json.dumps(json_data, indent=4)
#print (json_dump)

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

    cur.execute(
        'INSERT INTO Games VALUES (?,?,?,?,?,?,?,?,?,?)', 
        (id, title, thumbnail, short_description, game_url, 
        genre,platform, publisher, developer, release_date,)
        )
connection.commit()
