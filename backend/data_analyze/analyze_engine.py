from vcs_api.github_api import GithubAPI
from data_analyze.libraries.libraries_data import libraries
from .functions_finder import find_functions
import ast
from .Fun_finder import Call_finder


def analyze_file(file: object, language: str) -> list[object]:
    one_file_results = []
    for library in file["libraries"]:
        context = GithubAPIFacade.get_context_from_file(file["file"])
        tree = ast.parse(context, mode='exec')
        finder = Call_finder(language=language, library=library)
        finder.visit(tree)
        algorithm_uses = finder.functions
        # algorithm_uses = find_functions(context, language, library)
        file_results = {
            "category": libraries[language][library]["category"],
            "library": library,
            "algorithms": algorithm_uses,
            "location": {"repo": file["repo"],
                         "path": file["file"].path}
        }
    return file_results


def analyze_all_files(files, language: str):
    all_files_results = []
    for file in files:
        all_files_results.append(analyze_file(file, language))
    return all_files_results
