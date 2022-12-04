from config import TOKEN
from vcs_api.github_api_facade import GithubAPIFacade
from extract_files.extract_by_libraries import extract_by_libraries_ast

g = GithubAPIFacade(TOKEN, "Beavers-linter")
print(extract_by_libraries_ast(g.get_files_from_organization(), ["hashlib"]))