from pathlib import Path
from time import ctime
import shutil

path = Path("learnpythonmosh/standard library/ecommerce/__init__.py")
# print(path.exists())
# path.rename("init.txt")
# path.unlink()
print(path.stat())
print(ctime(path.stat().st_ctime))

print(path.read_text())
# path.write_text("...blah blah")

source = Path("learnpythonmosh/standard library/ecommerce/__init__.py")
target = Path() / "learnpythonmosh/quiz/__init__.py"

# target.write_text(source.read_text())
# Or
shutil.copy(source, target)
print(target.absolute())
