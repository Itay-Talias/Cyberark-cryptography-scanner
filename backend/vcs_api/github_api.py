from github import Github,Organization,Repository,ContentFile


def connect_to_github(token: str, organization: str) -> Organization:
    return Github(token).get_organization(organization)


def get_repos(organization: Organization) -> Repository:
    return organization.get_repos()


def get_context_from_file(file: ContentFile):
    return file.decoded_content.decode("utf-8")


def get_all_files_from_dir(repo: Repository,path: str,list_file: list[object]):
    for file in repo.get_dir_contents(path):
        if file.type=="file" :
            list_file.append({"repo":repo.full_name,"path":path,"file":file})
        elif file.type=="dir" :
            get_all_files_from_dir(repo,file.path,list_file)


def get_files_from_organization(token: str ,organization: str) -> list[object]:
    org = connect_to_github(token,organization)
    list_file = []
    for repo in get_repos(org):
        get_all_files_from_dir(repo, "/", list_file)
    return list_file
