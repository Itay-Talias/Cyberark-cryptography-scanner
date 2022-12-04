import json

from github import ContentFile
from vcs_api.github_api import get_context_from_file
from data_analyze.libraries.libraries_data import libraries


def analyze_file(file: object, language: str) -> list[object]:
    results = []
    for library in file["libraries"]:
        words_list = libraries[language][library]["words"]
        context = get_context_from_file(file["file"])
        split_context = context.splitlines()
        for word in words_list:
            for index, line in enumerate(split_context):
                # analyze word
                if word in line:
                    record = {"category": libraries[language][library]["category"],
                              "library": library,
                              "algorithm": word,
                              "location": {"repo": file["repo"],
                                           "path": file["file"].path,
                                           "line_index": index + 1}}
                    results.append(record)
    return results
