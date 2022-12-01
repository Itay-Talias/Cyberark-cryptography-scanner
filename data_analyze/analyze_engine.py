from github import ContentFile
from github_dir.github_handler import get_context_from_file
from data_analyze.libraries.python_libraries import hashlib_data


def analyze_file(file: ContentFile, library: str) -> list[object]:
    words_list = (list(map(lambda word: word["word"], hashlib_data.words)))
    context = get_context_from_file(file)
    for word in words_list:
        if word in context:
            print(word)
    return []
