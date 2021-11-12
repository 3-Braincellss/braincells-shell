def prettify_path(path):
    """Prettifies a given path"""
    words = []
    words = path.split("/")
    words.pop(0)
    for i in range(len(words) - 1):
        words[i] = words[i][0]
    ret = "/".join(words)
    return ret
