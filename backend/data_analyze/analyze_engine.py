from vcs_api.github_api import GithubAPI
from database.data.libraries_data import data
import ast
from .functoins_finder import Call_finder
from database.dal_mongo import DALMongoDB


def analyze_file(file: object, language: str, library: str, connector: DALMongoDB) -> list[object]:
    context = GithubAPI.get_context_from_file(file["file"])
    tree = ast.parse(context, mode='exec')
    finder = Call_finder(connector.get_functions_words_from_libraries(language, library))
    finder.visit(tree)
    algorithm_uses = finder.functions
    algorithm_uses = list(map(lambda a: create_algorithm_details(language, library, a, connector), algorithm_uses))
    file_results = {
        "success": file["success"],
        "category": data[language][library]["category"],
        "library": library,
        "algorithms": algorithm_uses,
        "url": file["url"],
        "location": {"repo": file["repo"],
                     "path": file["file"].path}
    }
    return file_results


def analyze_all_files(files, language: str, connector: DALMongoDB):
    all_files_results = []
    for file in files:
        if file["success"]:
            for library in file["libraries"]:
                all_files_results.append(analyze_file(file, language, library, connector))
        else:
            all_files_results.append(
                {"success": file["success"],
                 "url": file["url"],
                 "location": {"repo": file["repo"],
                              "path": file["file"].path}})
    return all_files_results


def create_algorithm_details(language: str, library: str, algorithm: object, connector: DALMongoDB):
    details = {**connector.get_function_details(language, library, algorithm["name"]), "line-index": algorithm["line-index"]}
    if algorithm["key_size"] != -1:
        details["key_size"] = f'{algorithm["key_size"]} bit'
    return details
