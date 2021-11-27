from exceptions.app_run import AppRunException

from glob import glob


def prettify_path(path):
    """Prettifies a given path"""
    words = []
    words = path.split("/")
    words.pop(0)
    for i in range(len(words) - 1):
        words[i] = words[i][0]
    ret = "/".join(words)
    return ret


def simple_globbing(args):
    return_args = []
    for each in args:
        globbing = glob(each)
        if globbing:
            return_args.extend(globbing)
        else:
            return_args.append(each)

    return return_args


def read_from_file(path, app_str):
    """
    Reads from a file and returns its contents
    :param path: The path of the file to be read.
    """
    try:
        with open(path, "r") as f:
            text = f.read()
            return text

    except OSError:
        raise AppRunException(app_str, f"{path}: No such file or directory\n")
    except IsADirectoryError:
        raise AppRunException(app_str, f"{path}: Is a directory")


def read_lines_from_file(path, app_str):
    """
    Reads from a file and returns the lines of the file.
    :param path: The path of the file to be read.
    """
    try:
        with open(path, "r") as f:
            text = f.readlines()
            return text

    except OSError:
        raise AppRunException(app_str, f"{path}: No such file or directory\n")
    except IsADirectoryError:
        raise AppRunException(app_str, f"{path}: Is a directory")
