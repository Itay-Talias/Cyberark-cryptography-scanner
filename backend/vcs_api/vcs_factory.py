from .vsc_api_facade import VscAPIFacade
from .github_api_facade import GithubAPIFacade


def create_vcs_connector( token: str, organization: str, vcs_type: str) -> VscAPIFacade:
    if vcs_type == "github":
        return GithubAPIFacade(token=token,organization=organization)