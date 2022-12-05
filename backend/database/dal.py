from abc import ABC, abstractmethod
from typing import List


class DAL(ABC):
    @abstractmethod
    def get_data_by_organization(self, organization_name: str) -> List[object]:
        pass

    @abstractmethod
    def get_data_by_repository(self, repository_name: str) -> List[object]:
        pass

    @abstractmethod
    def get_data_by_file(self, file_name: str) -> List[object]:
        pass

    @abstractmethod
    def add_library(self, library_name: str, language_id: int, category: int) -> None:
        pass

    @abstractmethod
    def add_word(self, word: str) -> None:
        pass

    @abstractmethod
    def add_language(self, language_name: str) -> None:
        pass

    @abstractmethod
    def get_scan_status(self) -> bool:
        pass