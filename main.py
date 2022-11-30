from config import token
from Github.github import get_files_from_organization, get_context_from_file


files = get_files_from_organization(token, "Beavers-linter")
for file in files:
    print("file name: ", file)
    print("configtext: ", get_context_from_file(file["file"]))
