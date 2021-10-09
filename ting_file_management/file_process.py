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
            return sys.stdout.write("Arquivo repetido")
    instance.enqueue(result)
    return sys.stdout.write(f"{result}")


def remove(instance):
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")
    else:
        removed_file = instance.dequeue()["nome_do_arquivo"]
        str = f"Arquivo {removed_file} removido com sucesso\n"
        return sys.stdout.write(str)


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        return sys.stdout.write(f"{result}")
    except IndexError:
        return sys.stderr.write("Posição inválida")
