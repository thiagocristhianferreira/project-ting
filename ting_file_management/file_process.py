import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content = txt_importer(path_file)
    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
    }
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return False
    instance.enqueue(result)
    return sys.stdout.write(f"{result}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
