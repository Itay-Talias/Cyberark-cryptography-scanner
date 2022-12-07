import ast
from .libraries.libraries_data import libraries


def find_functions(source: str, language: str, library: str):
    functions_uses = []
    tree = ast.parse(source, mode='exec')
    for node in ast.walk(tree):
        if (
                isinstance(node, ast.Call)  # It's a call
                and isinstance(node.func, ast.Attribute)
                and is_lib_function(node.func.attr, library, language)
                ):
            functions_uses.append({"line-index":node.lineno, "name":node.func.attr})
        elif (isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
                 and is_lib_function(node.func.id, library, language)):
                functions_uses.append({"line-index": node.lineno, "name": node.func.id})

    return functions_uses
def is_lib_function(func: str, library: str, language: str) -> bool:
    functions_list = libraries[language][library]["words"]
    return func in functions_list
