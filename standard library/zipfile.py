from pathlib import Path
from zipfile import ZipFile

working_dir = "learnpythonmosh/standard library/ecommerce/"

# with ZipFile(working_dir + "files.zip", "w") as zip:
#     for path in Path(working_dir).rglob("*.*"):
#         zip.write(path)


with ZipFile(working_dir + "files.zip", "r") as zip:
    print(zip.namelist())
    info = zip.getinfo("learnpythonmosh/standard library/ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("learnpythonmosh/standard library/ecommerce/extract")
