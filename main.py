from config import token
from vcs_api.github_api import get_files_from_organization
from mapping_files.mapping_reducer import mapping_files


f = get_files_from_organization(token, "Beavers-linter")
print(mapping_files(f))

