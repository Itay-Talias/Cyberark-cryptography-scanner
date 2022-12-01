import ast
from Import_finder import ImportFinder

def extract_by_libraries(filelist: list[object], libraries: list[str]) -> list[object]:
    map_list = list(map(lambda file: libraries_mapping(file, libraries), filelist))
    return list(filter(filter_empty_libraries, map_list))

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
    map_list = list(map(lambda file: libraries_mapping_ast(file, libraries), filelist))
    return list(filter(filter_empty_libraries, map_list))

def libraries_mapping_ast(file: object, libraries: list[str]) -> object:
    libraries_in_file = set()
    for library in libraries:
        file_context = file["file"].decoded_content.decode("utf-8").split()
        if is_file_import_lib (library, file_context):
            libraries_in_file.add(library)
    file["libraries"] = libraries_in_file
    return file

def is_file_import_lib(library : str, file_context : str) -> bool :
    import_names = parse_imports(file_context)
    return library in import_names

def parse_imports(source):
    tree = ast.parse(source)
    finder = ImportFinder()
    finder.visit(tree)
    return finder.imports