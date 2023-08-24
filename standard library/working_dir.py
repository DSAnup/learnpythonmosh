from pathlib import Path

path = Path("learnpythonmosh/standard library/ecommerce")
print(path.exists())
print(path.absolute())
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# for p in path.iterdir():
#     print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
# Find the all py file recursavely
py_files = [p for p in path.rglob("*.py")]
print(paths)
print(py_files)
