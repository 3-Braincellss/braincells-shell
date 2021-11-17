def prettify_path(path):
    """Prettifies a given path"""
    words = []
    words = path.split("/")
    words.pop(0)
    for i in range(len(words) - 1):
        words[i] = words[i][0]
    ret = "/".join(words)
    return ret

def read_from_file(path, app_str):
    """
    Reads from a file and returns its contents
    :param path: The path of the file to be read.
    """
    try:
        with open(path, "r") as f:
            text = f.read()
            return text
    except FileNotFound:
        raise AppRunException(app_str, f"{path}: No such file or directory")
