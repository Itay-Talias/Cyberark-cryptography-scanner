
def mapping_files(filelist: list[object],libraries_name: list[str]) -> list[object]:
   return list(map(mapping_file,filelist,libraries_name))


def mapping_file(file: object,libraries_name: list[str]) -> object:
    print("--------")
    libraries_in_file= set()
    for library in libraries_name:
        if library in file["file"].decoded_content.decode("utf-8").split():
            libraries_in_file.add(library)
        file["libraries"] = libraries_in_file
        return file
