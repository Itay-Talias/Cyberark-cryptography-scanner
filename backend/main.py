from config import TOKEN
from vcs_api.github_api import GithubAPIFacade
from extract_files.extract_by_libraries import extract_by_libraries
g = GithubAPIFacade(TOKEN, "Beavers-linter")
print(extract_by_libraries(g.get_files_from_organization(),["hashlib"]))
