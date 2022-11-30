from config import token
from Github.github import get_files_from_organization

get_files_from_organization(token, "Beavers-linter")
