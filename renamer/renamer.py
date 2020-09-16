#!/usr/bin/python3

import getopt
import glob
import sys
from datetime import datetime
import os
from typing import List, Dict

PREFIX = 'prefix'
EXTENSION = 'extension'
PATH = 'path'
REVERSE = 'reverse'

def main() -> None:
    opts, args = get_opts_args(sys.argv[1:])
    parameters = parse_parameters(opts, args)
    list_of_files = get_list_of_files(parameters)
    rename_files(list_of_files, parameters)


def get_list_of_files(parameters: Dict) -> List:
    list_of_files = glob.glob(f"{parameters[PATH]}/*.{parameters[EXTENSION]}")
    if parameters[REVERSE]:
        list_of_files.reverse()

    return list_of_files


def rename_files(list_of_files: List, parameters: Dict) -> None:
    index = 0
    for file in list_of_files:
        creation_date = get_creation_date(file)
        file_name = f"%s_%s_%03d.%s" % (parameters[PREFIX], creation_date, index, parameters[EXTENSION])
        os.rename(file, f"{parameters[PATH]}/{file_name}")
        index += 1


def get_creation_date(file_path: str) -> str:
    creation_timestamp = os.path.getctime(file_path)
    date = datetime.fromtimestamp(creation_timestamp)\

    return date.strftime('%Y-%m-%d')


def print_help() -> None:
    print('USAGE: renamer.py [OPTIONS] DIRECTORY')
    print('Renaming all files with configured extension to "<prefix>_<datestamp>_<counter>.<extension>" format')
    print('Options:')
    print('\t-p, --prefix\tPrefix of renamed file\t\t\tDefault: "audiofile"')
    print('\t-e, --extension\tExtension of files to be renamed\tDefault: "wav"')
    sys.exit()


def parse_parameters(opts: List, args: List) -> Dict:
    parameters = {
        PREFIX: 'audiofile',
        EXTENSION: 'wav',
        PATH: '',
        REVERSE: False
    }

    for current_argument, current_value in opts:
        if current_argument in ("-h", "--help"):
            print_help()
        elif current_argument in ("-p", "--prefix"):
            parameters[PREFIX] = current_value
        elif current_argument in ("-e", "--extension"):
            parameters[EXTENSION] = current_value
        elif current_argument in ("-r", "--reverse"):
            parameters[REVERSE] = True

    if not args:
        print_help()

    parameters[PATH] = args[0]

    return parameters


def get_opts_args(argument_list: List):
    short_options = "hrp:e:"
    long_options = ["help", "reverse", "prefix=", "extension="]

    return getopt.getopt(argument_list, short_options, long_options)


if __name__ == '__main__':
    main()
