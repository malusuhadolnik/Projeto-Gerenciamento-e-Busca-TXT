# Projeto-Gerenciamento-e-Busca-TXT

# Sobre
Este projeto consiste em uma simulação de um algoritmo de indexação de documentos, capaz de identificar ocorrências de termos em arquivos TXT, contando com dois módulos:

- Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT) e;
- Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.

##  Arquivos desenvolvidos

1. No arquivo ting_file_management/queue.py:
- Implementação da classe Queue para armazenar em uma fila arquivos TXT que serão lidos posteriormente;
- Inclui métodos para inserir e retirar arquivos da lista, verificar a existência de arquivos por índice e por path_file.

2. No arquivo ting_file_management/file_management.py: 
- Implementação da função  txt_importer, capaz de importar o conteúdo de um arquivo TXT;
- Recebe como input o caminho para o arquivo, e retorna uma lista com o conteúdo de cada linha do arquivo (i.e. cada linha é guardada em um array);

3. No arquivo ting_file_management/file_process.py: 
- Implementação da função process, que transforma o conteúdo da lista gerada pela função txt_importer em um dicionário, que por sua vez será armazenado dentro da Queue;
- Recebe como input o caminho para o arquivo e uma instância da classe Queue. 

4. No arquivo ting_file_management/file_process.py: 
- Implementação da função remove, que remove um arquivo da fila.
- Recebe como input uma instância da classe Queue.

5. No arquivo ting_file_management/file_process.py: 
- Implementação da função file_metadata, que imprime os metadados do arquivo cujo índice é alvo da consulta
- Recebe como input uma instância da classe Queue e o índex referente ao arquivo alvo.

6. No arquivo ting_word_searches/word_search.py: 
- Implementação da função exists_word, que realiza uma busca case-insensitive de uma determinada palavra em todos os textos da lista
- Recebe como input uma instância da classe Queue e a palavra buscada.
- Retornar uma lista com o nome de cada arquivo e suas linhas em que a palavra foi encontrada.

7. No arquivo ting_word_searches/word_search.py: 
- Implementação da função search_by_word, que realiza uma busca case-insensitive de uma determinada palavra em todos os textos da lista
- Recebe como input uma instância da classe Queue e a palavra buscada.
- Retornar uma lista com o nome de cada arquivo, as linhas em que a palavra foi encontrada, e o conteúdo da linha.

Os demais arquivos foram desenvolvidos pelo time da Trybe.

## Habilidades exercitadas
- Manipular Pilhas;
- Manipular Deque;
- Manipular Nó & Listas Ligadas e;
- Manipular Listas Duplamente Ligadas.

## Tecnologias usadas
Python
