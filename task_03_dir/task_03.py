import sys
from pathlib import Path
from colorama import Fore


def pretty_print(path: str, indent: int = 0) -> None:
    directory = Path(path)
    for x in directory.iterdir():
        indent_prefix = " " * indent * 2
        if x.is_dir():
            print(Fore.RED + indent_prefix + x.name)
            pretty_print(path + "/" + x.name, indent + 1)
        else:
            print(Fore.BLUE + indent_prefix + x.name)


pretty_print(sys.argv[1])
