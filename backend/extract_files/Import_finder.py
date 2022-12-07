import ast

class Import_finder(ast.NodeVisitor):
    def __init__(self):
        self.imports = []

    def visit_Import(self, node):
        names = []
        for i in node.names:
            names.append(i.name)
        self.imports.append(names)

    def visit_ImportFrom(self, node):
        module = node.module
        names = []
        for i in node.names:
            if(i.name != "*"):
                names.append(f'{module}.{i.name}')
            else:
                names.append(module)
        self.imports.append(names)

