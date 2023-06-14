# Bibliografia consultada:
# https://stackoverflow.com/questions/16506429/check-if-element-is-already-in-a-queue

import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    #  checar se arquivo já existe na fila
    if instance.is_in_queue(path_file) is True:
        return None

    # agora criamos nossa fila com o caminho dado
    target_file = txt_importer(path_file)
    # e se for criada com sucesso, usamos seus dados para criar o dict
    if target_file:
        files_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(target_file),
            "linhas_do_arquivo": target_file,
        }
        instance.enqueue(files_dict)
        print(files_dict, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        target_file = instance.dequeue()
        print(f"Arquivo {target_file['nome_do_arquivo']} removido com sucesso",
              file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
