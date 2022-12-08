import ast

class Call_finder(ast.NodeVisitor):
    def __init__(self, functions_words: list[str]):
        self.functions = []
        self.functions_words = functions_words

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            while not hasattr(node.func, "value") and isinstance(node.func.value, ast.Call):
                node = node.func.value
        key_size = -1
        for keyword in node.keywords:
            if keyword.arg == "key_size":
                key_size = keyword.value.value
            # elif isinstance(keyword.value,ast.Call):
            #     self.visit(keyword.value)
        if (
                isinstance(node.func, ast.Attribute)
                and self.is_lib_function(node.func.attr)
        ):
            self.adding_function_to_list(node.lineno,node.func.attr,key_size)
        elif (isinstance(node.func, ast.Name)
              and self.is_lib_function(node.func.id)):
            self.adding_function_to_list(node.lineno,node.func.id,key_size)
        # for arg in node.args:
        #     if isinstance(arg, ast.Call):
        #         self.visit(arg)


    def is_lib_function(self, func: str) -> bool:
        return func in self.functions_words

    def adding_function_to_list(self, line: str, name:str, key_size:int):
        self.functions.append({"line_index": line, "name": name, "key_size": key_size})

