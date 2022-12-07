from .vsc_api import VscAPI
from .github_api import GithubAPI
from enum import Enum

class Vcs_type(Enum):
    github = "github"

def create_vcs_connector( token: str, organization: str, vcs_type: str) -> VscAPI:
    if vcs_type == Vcs_type.github.value:
        return GithubAPI(token = token, organization = organization)