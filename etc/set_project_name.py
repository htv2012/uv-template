import pathlib
import re


def edit_file(filename: str, search: str, replace: str):
    file = pathlib.Path(filename)
    content = file.read_text()
    content = re.sub(rf"\b{search}\b", replace, content)
    print(content)
    file.write_text(content)


print("Changing project name from xyz to a new name")
dash_name = input("New name: ")
under_name = dash_name.replace("-", "_")

edit_file("pyproject.toml", "xyz", dash_name)
edit_file("Makefile", "xyz", dash_name)
edit_file("src/xyz/cli.py", "xyz", dash_name)

package_dir = pathlib.Path("src/xyz")
package_dir.rename(f"src/{under_name}")
