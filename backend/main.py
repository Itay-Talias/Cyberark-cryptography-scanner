from config import TOKEN
from vcs_api.github_api import get_files_from_organization
from data_analyze.analyze_engine import analyze_file
from github import ContentFile

files = get_files_from_organization(TOKEN, "Beavers-linter")

for file in files:
    file["libraries"] = {'hashlib', 'bcrypt'}
    analyze_file(file, "python")
