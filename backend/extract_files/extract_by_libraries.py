import ast
from extract_files.Import_finder import Import_finder
code_files_suffix = {"py"}
def filter_empty_libraries(file: object) -> bool:
    if len(file["libraries"]) > 0 or not file["success"]:
        return True

    return False

def extract_by_libraries_ast(filelist: list[object], libraries: list[str]) -> list[object]:
    filtered_code_filelist = list(filter(lambda file: file["file"].name.rsplit('.', 1)[-1] in code_files_suffix, filelist))
    map_list = list(map(lambda file: libraries_mapping_ast(file, libraries), filtered_code_filelist))
    filtered_list = list(filter(filter_empty_libraries, map_list))
    return filtered_list

def libraries_mapping_ast(file: object, libraries: list[str]) -> object:
    try:
        file_context = file["file"].decoded_content.decode("utf-8")
        libraries_in_file = file_import_lib(file_context)
        libraries_in_file = libraries_in_file.intersection(set(libraries))
        file["libraries"] = libraries_in_file
        file["success"] = True
    except SyntaxError:
        file["libraries"] = []
        file["success"] = False
    return file

def file_import_lib(file_context : str) -> set[str]:
    libraries_in_file = set()
    imports = parse_imports(file_context)
    for import_obj in imports:
        for library in import_obj:
            libraries_in_file.add(library)
    return libraries_in_file

def parse_imports(source):
    tree = ast.parse(source, mode='exec')
    finder = Import_finder()
    finder.visit(tree)
    return finder.imports
