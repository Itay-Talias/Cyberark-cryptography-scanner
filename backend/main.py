from config import TOKEN
from vcs_api.github_api import GithubAPIFacade
# from data_analyze.analyze_engine import analyze_file

g = GithubAPIFacade(TOKEN, "Beavers-linter")
print(g.get_files_from_organization())
