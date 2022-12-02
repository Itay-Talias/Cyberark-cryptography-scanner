from .vsc_api_facade import VscAPIFacade
from .github_api_facade import GithubAPIFacade
from enum import Enum

class Vcs_type(Enum):
    github = "github"

def create_vcs_connector( token: str, organization: str, vcs_type: str) -> VscAPIFacade:
    if vcs_type == Vcs_type.github.value:
        return GithubAPIFacade(token = token, organization = organization)