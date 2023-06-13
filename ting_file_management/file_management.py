# Bibliografia consultada:
# https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
# https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/
# https://www.w3schools.com/python/python_try_except.asp
# https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/

import sys
import pathlib


def txt_importer(path_file):
    extension = pathlib.Path(path_file).suffix
    if extension != '.txt':
        sys.stderr.write("Formato inválido")

    try:
        opened_file = open(path_file, 'r')
        read_the_file = opened_file.read()
        text_list = read_the_file.split("\n")
        return text_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
