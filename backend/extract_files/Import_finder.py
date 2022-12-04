import ast

class Import_finder(ast.NodeVisitor):
    def __init__(self):
        self.imports = []

    def visit_Import(self, node):
        names = []
        for i in node.names:
            names.append(i.name)
        self.imports.append(['import', names])

    def visit_ImportFrom(self, node):
        module = node.module
        level = node.level  # how many dots
        names = []
        for i in node.names:
            names.append(i.name)

        self.imports.append(('from', level, module, names))

