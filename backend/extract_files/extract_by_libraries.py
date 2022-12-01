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
