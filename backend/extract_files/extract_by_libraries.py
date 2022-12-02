import ast
from backend.extract_files.Import_finder import Import_finder
code_files_suffix = {"py"}
def extract_by_libraries(filelist: list[object], libraries: list[str]) -> list[object]:
    map_list = list(map(lambda file: libraries_mapping(file, libraries), filelist))
    filterd_list = list(filter(filter_empty_libraries, map_list))
    return filterd_list

def libraries_mapping(file: object, libraries: list[str]) -> object:
    libraries_in_file = set()
    for library in libraries:
        if library in file["file"].decoded_content.decode("utf-8").split():
            libraries_in_file.add(library)

    file["libraries"] = libraries_in_file
    return file

def filter_empty_libraries(file: object) -> bool:
    if len(file["libraries"]) > 0:
        return True

    return False

def extract_by_libraries_ast(filelist: list[object], libraries: list[str]) -> list[object]:
    filterd_code_filelist = list(filter(lambda file:file["file"].name.rsplit('.', 1)[-1] in code_files_suffix, filelist))
    map_list = list(map(lambda file: libraries_mapping_ast(file, libraries), filterd_code_filelist))
    filterd_list = list(filter(filter_empty_libraries, map_list))
    return filterd_list

def libraries_mapping_ast(file: object, libraries: list[str]) -> object:
    libraries_in_file = set()
    for library in libraries:
        file_context = file["file"].decoded_content.decode("utf-8")
        if is_file_import_lib (library, file_context):
            libraries_in_file.add(library)
    file["libraries"] = libraries_in_file
    return file

def is_file_import_lib(library : str, file_context : str) -> bool :
    imports_names = []
    imports = parse_imports(file_context)
    for import_obj in imports:
        libs_names : list[str] = import_obj[1][0]
        imports_names.append(libs_names)

    res = any(library in libs_names for libs_names in imports_names)
    return res

def parse_imports(source):
    tree = ast.parse(source, mode = 'exec')
    finder = Import_finder()
    finder.visit(tree)
    return finder.imports