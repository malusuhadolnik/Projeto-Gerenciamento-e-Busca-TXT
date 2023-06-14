def exists_word(word, instance):
    output = list()
    for i in range(len(instance)):
        # 1a iteração usando search, um método da Queue (dica da monitoria)
        # Para cada índice (texto) da lista, será criada uma lista iterável
        smp_txt = instance.search(i)
        # Criamos o dict antes de entrar na linha, para poder guardar + de 1
        retrieved_data = {
            "palavra": word,
            "arquivo": smp_txt["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line in smp_txt["linhas_do_arquivo"]:
            if word.lower() in line.lower():  # lower() para passar no teste
                retrieved_data["ocorrencias"].append(
                      {"linha": smp_txt["linhas_do_arquivo"].index(line) + 1}
                )
        if retrieved_data["ocorrencias"]:  # só inclui se achar a palavra
            output.append(retrieved_data)
        return output


def search_by_word(word, instance):
    output = list()
    for i in range(len(instance)):
        smp_txt = instance.search(i)
        retrieved_data = {
            "palavra": word,
            "arquivo": smp_txt["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line in smp_txt["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                retrieved_data["ocorrencias"].append(
                    {
                        "linha": smp_txt["linhas_do_arquivo"].index(line) + 1,
                        "conteudo": line
                    }
                )
        if retrieved_data["ocorrencias"]:
            output.append(retrieved_data)
        return output
