def mapping_files(filelist: list[object]) -> list[object]:
    map_list = list(map(mapping_file, filelist))
    return list(filter(filter_file,map_list))


def mapping_file(file: object) -> object:
    libraries_name = ["hashlib"]
    libraries_in_file = set()
    for library in libraries_name:
        if library in file["file"].decoded_content.decode("utf-8").split():
            libraries_in_file.add(library)

    file["libraries"] = libraries_in_file
    return file

def filter_file(file: object) -> bool:
    if len(file["libraries"]) > 0:
        return True

    return False