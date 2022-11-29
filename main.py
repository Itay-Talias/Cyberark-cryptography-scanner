from github import Github
from config import token
g = Github(token)

org = g.get_organization("Beavers-linter")
for repo in org.get_repos():
    print(f"""Name of repo - {repo}
    ===============================
    """)
    files = repo.get_contents("")
    print(f"""{files}
    =========================
    =========================
    """)
    for file in files:
        file_context = file.decoded_content.decode("utf-8")
