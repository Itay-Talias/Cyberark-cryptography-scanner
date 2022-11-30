from github import Github,Organization,Repository,ContentFile


def connect_to_github(token: str, organization: str) -> Organization:
    return Github(token).get_organization(organization)


def get_repos(organization: Organization) -> Repository:
    return organization.get_repos()


def get_files_from_repo(repo: Repository) -> list[ContentFile]:
    return repo.get_contents("")


def get_context_from_file(file: ContentFile):
    return file.decoded_content.decode("utf-8")


def print_all_files_in_organization(token: str ,organization: str):
    org = connect_to_github(token,organization)
    for repo in get_repos(org):
        print(f'Name of repo - {repo}')
        files = get_files_from_repo(repo)
        print(f'{files}')