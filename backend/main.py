from config import TOKEN
from vcs_api.github_api import get_files_from_organization
from mapping_files.mapping_reducer import mapping_files


f = get_files_from_organization(TOKEN, "Beavers-linter")
print(mapping_files(f, ["hashlib", "bycrypt"]))
