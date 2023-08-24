import sqlite3
import json
from pathlib import Path


working_dir = "learnpythonmosh/standard library/ecommerce/"

movies = json.loads(Path(working_dir + "movies.json").read_text())
print(movies)

# for movie in movies:
#     print(tuple(movie.keys()))

# Insert
# with sqlite3.connect(working_dir + "db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# SELECT

with sqlite3.connect(working_dir + "db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
