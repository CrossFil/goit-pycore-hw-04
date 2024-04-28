'''Home work 3'''

import sys

from pathlib import Path
from colorama import Fore # type: ignore



def file_parcer(path, spaces=0):
    '''Function parc file directory'''
    for el in path.iterdir():
        if el.is_file():
            print(Fore.GREEN + ' ' * spaces + el.name)
        elif el.is_dir():
            # spaces += 4
            print(Fore.BLUE + spaces * ' ' + el.name + '/')
            file_parcer(el, spaces+4)

if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print(Fore.RED + 'You should write path to folder')
        sys.exit()
    source_path = sys.argv[1] # отримання арг з консольного рядка


    path_directory = Path(source_path)
    if not path_directory.exists():
        print(Fore.RED + 'Directory not exist')
    elif not path_directory.is_dir():
        print(Fore.RED + 'wrong directory')
    else:
        file_parcer(path_directory)
