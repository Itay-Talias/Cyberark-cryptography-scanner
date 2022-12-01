from config import token
from github_dir.github_handler import get_files_from_organization
from mapping_files.mapping_reducer import mapping_files


f = get_files_from_organization(token, "Beavers-linter")
print(f)
print(mapping_files(f))

