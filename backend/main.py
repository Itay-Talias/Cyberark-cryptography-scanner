from config import TOKEN
from github_dir.github_handler import get_files_from_organization
from data_analyze.analyze_engine import analyze_file

files = get_files_from_organization(TOKEN, "Beavers-linter")
for file in files:
    analyze_file(file["file"], "python", "hashlib")
