from vcs_api.github_api import GithubAPI
from database.data.libraries_data import libraries_data
import ast
from .functoins_finder import Call_finder
from database.dal_mongo import DALMongoDB


def analyze_file(file: object, language: str, library: str, connector: DALMongoDB) -> list[object]:
    context = GithubAPI.get_context_from_file(file["file"])
    tree = ast.parse(context, mode='exec')
    finder = Call_finder(connector.get_functions_words_from_libraries(language, library))
    visit_tree(tree, finder)
    algorithm_uses = finder.functions
    algorithm_uses = list(map(lambda a: create_algorithm_details(language, library, a, connector), algorithm_uses))
    file_results = {
        "success": file["success"],
        "category": libraries_data[language][library]["category"],
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
    details = {**connector.get_function_details(language, library, algorithm["name"]), "line_index": algorithm["line_index"]}
    if algorithm["key_size"] != -1:
        details["key_size"] = f'{algorithm["key_size"]} bit'
    return details

def visit_tree(tree, finder):
    if isinstance(tree, ast.Module):
        for node in tree.body:
            visit_tree(node, finder)
    elif isinstance(tree, ast.Assign):
        for node in tree.targets:
            visit_tree(node, finder)
        visit_tree(tree.value, finder)
    elif isinstance(tree, ast.Expr):
        visit_tree(tree.value, finder)
    elif isinstance(tree, ast.Compare):
        visit_tree(tree.left, finder)
        for node in tree.ops:
            visit_tree(node, finder)
    elif isinstance(tree, ast.Attribute):
        visit_tree(tree.value, finder)
    elif isinstance(tree, ast.While):
        for node in tree.body:
            visit_tree(node, finder)
    elif isinstance(tree, ast.Try):
        for node in tree.body:
            visit_tree(node, finder)
        for node in tree.handlers:
            visit_tree(node, finder)
    elif isinstance(tree,ast.ExceptHandler):
        for node in tree.body:
            visit_tree(node, finder)
    elif isinstance(tree,ast.For):
        for node in tree.body:
            visit_tree(node, finder)
        visit_tree(tree.iter, finder)
        visit_tree(tree.target, finder)
    elif isinstance(tree,ast.With):
        for node in tree.body:
            visit_tree(node, finder)
    elif isinstance(tree, ast.While):
        for node in tree.body:
            visit_tree(node, finder)
        visit_tree(tree.test, finder)
    elif isinstance(tree, ast.If):
        for node in tree.body:
            visit_tree(node, finder)
        visit_tree(tree.test, finder)
    elif isinstance(tree, ast.With):
        for node in tree.body:
            visit_tree(node, finder)
        for node in tree.items:
            visit_tree(node, finder)
    elif isinstance(tree,ast.withitem):
        visit_tree(tree.context_expr, finder)
        visit_tree(tree.optional_vars, finder)
    elif isinstance(tree, ast.Call):
        finder.visit(tree)
        for arg in tree.args:
            if isinstance(arg, ast.Call):
                visit_tree(arg, finder)
        visit_tree(tree.func, finder)
        for keyword in tree.keywords:
            if isinstance(keyword.value, ast.Call):
                visit_tree(keyword.value, finder)
    else:
        finder.visit(tree)


