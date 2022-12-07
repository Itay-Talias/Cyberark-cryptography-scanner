from github import Github, Organization, Repository, ContentFile
from .vsc_api import VscAPI


class GithubAPI(VscAPI):

    def __init__(self, token: str, organization: str):
        super().__init__(organization=organization)
        self.github_connector = Github(token)

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
    def get_all_files_from_dir(repo: Repository, path: str, list_file: list[object]):
        for file in repo.get_dir_contents(path):
            if file.type == "file":
                list_file.append({"repo": repo.full_name, "path": path, "file": file, "url": file.html_url})
            elif file.type == "dir":
                GithubAPI.get_all_files_from_dir(repo, file.path, list_file)
