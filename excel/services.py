def validate_excel(files: tuple, extension: str) -> bool:
    """
    This function is used to validate if the files are xlsx files.
    :param files:
    :param extension:
    :return: boolean
    """
    for file in files:
        if not file.name.endswith(extension):
            return False
    return True
