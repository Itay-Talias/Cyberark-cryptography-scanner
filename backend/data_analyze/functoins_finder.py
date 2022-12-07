import ast
from database.data.libraries_data import data

class Call_finder(ast.NodeVisitor):
    def __init__(self, language, library):
        self.functions = []
        self.library = library
        self.language = language

    def visit_Call(self, node):
        if(isinstance(node.func, ast.Attribute)):
            while(isinstance(node.func.value, ast.Call)):
                node = node.func.value
        if (
                isinstance(node.func, ast.Attribute)
                and self.is_lib_function(node.func.attr)
        ):
            self.functions.append({"line-index": node.lineno, "name": node.func.attr})
        elif (isinstance(node.func, ast.Name)
              and self.is_lib_function(node.func.id)):
            self.functions.append({"line-index": node.lineno, "name": node.func.id})

    def is_lib_function(self,func: str) -> bool:
        functions_list = data[self.language][self.library]["words"]
        return func in functions_list
