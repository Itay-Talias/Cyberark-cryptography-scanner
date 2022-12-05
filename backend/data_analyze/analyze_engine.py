from vcs_api.github_api_facade import GithubAPIFacade
from data_analyze.libraries.libraries_data import libraries


def analyze_file(file: object, language: str) -> list[object]:
    one_file_results = []
    for library in file["libraries"]:
        words_list = libraries[language][library]["words"]
        context = GithubAPIFacade.get_context_from_file(file["file"])
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
                    one_file_results.append(record)
    return one_file_results


def analyze_all_files(files, language: str):
    all_files_results = []
    for file in files:
        all_files_results.append(analyze_file(file, language))
    return all_files_results
