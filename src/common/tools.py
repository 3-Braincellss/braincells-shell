"""
Tools
=====
"""
from exceptions import RunError

from glob import glob


def prettify_path(path):
    """Prettifies a given path

    Converts a given path like this:

    ``/home/mow/Documents/file.txt``

    Into this:

    ``/h/m/D/file.txt``

    Parameters:
        path(:obj:`str`): path to be prettified.

    Returns:
        :obj:`str`: A prettified path.

    """
    words = []
    words = path.split("/")
    words.pop(0)
    for i in range(len(words) - 1):
        words[i] = words[i][0]
    ret = "/".join(words)
    return ret


def simple_globbing(args):
    """Globs the list of given arguments and
    returns an extended list of globbed paths.

    Parameters:
        args(:obj:`list`): A list of paths to be globbed.
    Returns:
        :obj:`list`: A list of globbed paths.
    """
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
    Reads from a file and returns its contents.

    Parameters:
        path(:obj:`str`): The path of the file to be read.
        app_str(:obj:`str`): Name of the app that might cause the error.
    Returns:
        :obj:`str`: File contents
    Raises:
        RunError: If a given path is a directory or a given path doesn't exist.
    """

    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            return text

    except IsADirectoryError as err:
        raise RunError(app_str, f"{path}: Is a directory") from err

    except OSError as err:
        raise RunError(app_str,
                       f"{path}: No such file or directory\n") from err


def read_lines_from_file(path, app_str):
    """
    Reads from a file and returns the lines of the file.

    Parameters:
        path(:obj:`str`): The path of the file to be read.
        app_str(:obj:`str`): Name of the app that might cause the error.
    Returns:
        :obj:`list`: List of lines of the file.
    Raises:
        RunError: If a given path is a directory or a given path doesn't exist.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.readlines()
            return text

    except IsADirectoryError as err:
        raise RunError(app_str, f"{path}: Is a directory") from err

    except OSError as err:
        raise RunError(app_str,
                       f"{path}: No such file or directory\n") from err
