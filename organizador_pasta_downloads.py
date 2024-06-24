import os
import json
import shutil

# Caminho do diretório do projeto
caminho_projeto = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo JSON
caminho_json = os.path.join(caminho_projeto, 'configuracoes.json')

# Lendo o arquivo JSON
with open(caminho_json, 'r') as arquivo_json:
    configuracoes = json.load(arquivo_json)

# Obtendo o dicionário de pastas
pastas = configuracoes.get('pastas', {})

# Obtendo o caminho da pasta de Downloads no Windows
caminho_downloads = os.path.join(os.environ['USERPROFILE'], 'Downloads')

# Criando as pastas de destino se não existirem
for nome_pasta in pastas.keys():
    caminho_pasta = os.path.join(caminho_downloads, nome_pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

# Percorrendo os arquivos na pasta de downloads
for nome_arquivo in os.listdir(caminho_downloads):
    caminho_arquivo = os.path.join(caminho_downloads, nome_arquivo)

    # Verificando se é um arquivo (e não uma pasta)
    if os.path.isfile(caminho_arquivo):
        # Obtendo a extensão do arquivo
        _, extensao = os.path.splitext(nome_arquivo)

        # Tentando encontrar a pasta correspondente para a extensão
        for nome_pasta, extensoes in pastas.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(caminho_downloads, nome_pasta)
                # Tentando mover o arquivo para a pasta de destino
                try:
                    novo_caminho = os.path.join(destino, nome_arquivo)
                    shutil.move(caminho_arquivo, novo_caminho)
                    print(f'Movido: {nome_arquivo} para {destino}')
                except PermissionError:
                    print(f'Não foi possível mover o arquivo: {nome_arquivo}. Ele pode estar em uso.')
                break # Saindo do loop, já que encontramos a pasta correta e movemos o arquivo