from pathlib import Path
import json
import shutil
import logging

# Caminho do diretório do projeto
caminho_projeto = Path(__file__).parent.absolute()

# Configuração do logger
logging.basicConfig(
    filename=caminho_projeto / 'erros.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    encoding='utf-8'
)

# Caminho do arquivo JSON
caminho_json = caminho_projeto / 'configuracoes.json'

# Lendo o arquivo JSON
with open(caminho_json, 'r') as arquivo_json:
    configuracoes = json.load(arquivo_json)

# Obtendo o dicionário de pastas
pastas = configuracoes.get('pastas', {})

# Obtendo o caminho da pasta de Downloads no Windows
caminho_downloads = Path.home() / 'Downloads'

# Criando as pastas de destino se não existirem
for nome_pasta in pastas.keys():
    caminho_pasta = caminho_downloads / nome_pasta
    caminho_pasta.mkdir(exist_ok=True)

# Percorrendo os arquivos na pasta de downloads
for caminho_arquivo in caminho_downloads.iterdir():
    # Verificando se é um arquivo (e não uma pasta)
    if caminho_arquivo.is_file():
        # Obtendo a extensão do arquivo
        extensao = caminho_arquivo.suffix

        # Tentando encontrar a pasta correspondente para a extensão
        for nome_pasta, extensoes in pastas.items():
            if extensao.lower() in extensoes:
                destino = caminho_downloads / nome_pasta
                # Tentando mover o arquivo para a pasta de destino
                try:
                    novo_caminho = destino / caminho_arquivo.name
                    shutil.move(str(caminho_arquivo), str(novo_caminho))
                    print(f'Movido: {caminho_arquivo.name} para {destino}')
                except PermissionError:
                    mensagem_erro = f'Não foi possível mover o arquivo: {caminho_arquivo.name}. Ele pode estar em uso.'
                    print(mensagem_erro)
                    logging.error(mensagem_erro)
                except Exception as e:
                    mensagem_erro = f'Erro ao mover o arquivo {caminho_arquivo.name}. {str(e)}'
                    print(mensagem_erro)
                    logging.error(mensagem_erro)
                break # Saindo do loop, já que encontramos a pasta correta e movemos o arquivo
