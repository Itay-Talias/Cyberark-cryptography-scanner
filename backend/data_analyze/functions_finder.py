import ast


def find_function(source):
    tree = ast.parse(source, mode='exec')
    for node in ast.walk(tree):
        if (
                isinstance(node, ast.Call)  # It's a call
                and isinstance(node.func, ast.Attribute)
                and ("sha" in node.func.attr or "blake" in node.func.attr or "md" in node.func.attr or "scrypt" in node.func.attr)
                ):
            print(f"{node.lineno} : {node.func.value.id}.{node.func.attr}")
