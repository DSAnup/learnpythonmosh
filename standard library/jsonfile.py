import json
from pathlib import Path

working_dir = "learnpythonmosh/standard library/ecommerce/"

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "John wick", "year": 2003},
    {"id": 3, "title": "Krish", "year": 2005},
]

data = json.dumps(movies)

print(data)
Path(working_dir + "movies.json").write_text(data)
jsonread = Path(working_dir + "movies.json").read_text()
movies2 = json.loads(jsonread)
print(movies2[0])
print(movies2[0]["title"])
