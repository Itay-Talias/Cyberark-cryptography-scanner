def mapping_files(filelist: list[object]) -> list[object]:
    return list(map(mapping_file, filelist))


def mapping_file(file: object) -> object:
    libraries_name = ["hashlib"]
    libraries_in_file = set()
    for library in libraries_name:
        if library in file["file"].decoded_content.decode("utf-8").split():
            libraries_in_file.add(library)

    file["libraries"] = libraries_in_file
    return file
