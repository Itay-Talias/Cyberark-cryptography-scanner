import ast


def find_function(source):
    tree = ast.parse(source, mode='exec')
    for node in ast.walk(tree):
        if (
                isinstance(node, ast.Call)  # It's a call
                and isinstance(node.func, ast.Name)  # It directly invokes a name
                and node.func.id == 'update'  # That name is `print`
                ):
            # Check if any arg is the one we're looking for
            print(any(
                arg.value == "hard coded"
                for arg in node.args
                if isinstance(arg, ast.Constant)
                ))