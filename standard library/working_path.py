from pathlib import Path

Path("C:\\site\\columncheck\\")
# or
Path(r"C:\site\newfw1")

print(Path() / "modules")
print(Path.home())

path = Path("ecommerce/__init__.py")

print(path.exists())
print(path.is_file())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())
