from config import token
from Github.github import print_all_files_in_organization, get_files_from_repo,connect_to_github,get_repos, get_context_from_file

organization = connect_to_github(token, "Beavers-linter")
repos = get_repos(organization)
for repo in repos:
    files = get_files_from_repo(repo)
    for file in files:
        print("file:", file)
        context = get_context_from_file(file)
        context.split('\n')
        print("context:", context)
