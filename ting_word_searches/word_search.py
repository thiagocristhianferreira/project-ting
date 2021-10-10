def exists_word(word, instance):
    result = list()
    for index_file in range(len(instance)):
        get_file = instance.search(index_file)
        add_or_no = False
        lines = list()
        for index_line, line in enumerate(get_file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                add_or_no = True
                lines.append({'linha': index_line + 1})

        if add_or_no:
            result.append({
                'palavra': word,
                'arquivo': get_file['nome_do_arquivo'],
                'ocorrencias': lines
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
