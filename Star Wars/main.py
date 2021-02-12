import sqlite3
import ssl
import urllib.request
import json

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

service_url = "https://swapi.dev/api/people"
response = urllib.request.urlopen(service_url, context=context)
api_data = response.read().decode()

json_data = json.loads(api_data)
data = json_data["results"]

connection = sqlite3.connect("db.sqlite3")
cur = connection.cursor()
cur.execute("DROP TABLE IF EXISTS StarWars")
cur.execute(
    """CREATE TABLE StarWars(name, height, mass, hair_color,
            skin_color, eye_color, birth_year, gender);"""
)

for person in data:
    name = person["name"]
    height = person["height"]
    mass = person["mass"]
    hair_color = person["hair_color"]
    skin_color = person["skin_color"]
    eye_color = person["eye_color"]
    birth_year = person["eye_color"]
    gender = person["gender"]

    cur.execute(
        """INSERT INTO StarWars(name, height, mass,
                hair_color, skin_color, eye_color, birth_year, gender)
                VALUES (?,?,?,?,?,?,?,?)""",
        (
            name,
            height,
            mass,
            hair_color,
            skin_color,
            eye_color,
            birth_year,
            gender,
        ),
    )

    connection.commit()
