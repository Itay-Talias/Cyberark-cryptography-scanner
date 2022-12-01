from abc import ABC, abstractmethod


class VscAPIFacade(ABC):
    @abstractmethod
    def __init__(self, organization: str):
        self.organization = organization

    @abstractmethod
    def get_organization(self):
        pass

    @abstractmethod
    def get_repos_of_organization(self):
        pass

    @abstractmethod
    def get_files_from_organization(self) -> list[object]:
        pass

