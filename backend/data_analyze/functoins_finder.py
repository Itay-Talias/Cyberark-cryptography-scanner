import ast

class Call_finder(ast.NodeVisitor):
    def __init__(self, functions_words: list[str]):
        self.functions = []
        self.functions_words = functions_words

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
        return func in self.functions_words
