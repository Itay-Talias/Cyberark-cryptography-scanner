from github import Github,Organization,Repository,ContentFile
from file import File


class GithubAPIFacade:
    def __init__(self, token: str, organization: str):
        self.github_connector = Github(token)
        self.organization = organization

    def get_organization(self) -> Organization:
        return self.github_connector.get_organization(self.organization)

    def get_repos_of_organization(self) -> Repository:
        return self.get_organization().get_repos()

    def get_files_from_organization(self) -> list[object]:
        list_file = []
        for repo in self.get_repos_of_organization():
            self.get_all_files_from_dir(repo, "/", list_file)
        return list_file

    @staticmethod
    def get_context_from_file(file: ContentFile):
        return file.decoded_content.decode("utf-8")

    @staticmethod
    def get_all_files_from_dir(repo: Repository,path: str,list_file: list[object]):
        for file in repo.get_dir_contents(path):
            if file.type == "file":
                list_file.append(File())
            elif file.type == "dir":
                GithubAPIFacade.get_all_files_from_dir(repo, file.path, list_file)


