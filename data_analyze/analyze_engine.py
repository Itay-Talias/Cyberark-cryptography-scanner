from github import ContentFile
from github_dir.github_handler import get_context_from_file
from data_analyze.libraries.libraries_data import libraries


def analyze_file(file: ContentFile, language: str, library: str) -> list[object]:
    words_list = libraries[language][library]["words"]
    context = get_context_from_file(file)
    for word in words_list:
        if word in context:
            print(word)
    return []
