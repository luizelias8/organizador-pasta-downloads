from pathlib import Path
import json
import shutil
import logging

# Caminho do diretório do projeto
caminho_projeto = Path(__file__).parent.absolute()

# Caminho do arquivo JSON
caminho_json = caminho_projeto / 'configuracoes.json'

# Obtendo o caminho da pasta de Downloads no Windows
caminho_downloads = Path.home() / 'Downloads'

# Configuração do logger
def configurar_logger():
    logging.basicConfig(
        filename=caminho_projeto / 'erros.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',
        encoding='utf-8'
    )

# Lendo o arquivo JSON e retornando as configurações
def carregar_configuracoes():
    with open(caminho_json, 'r') as arquivo_json:
        return json.load(arquivo_json)

# Criar pasta de destino sob demanda
def criar_pasta(destino):
    if not destino.exists():
        destino.mkdir()
        print(f'Pasta criada: {destino}')

# Mover o arquivo para a pasta de destino
def mover_arquivo(caminho_arquivo, destino):
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

# Processar arquivos no diretório de downloads
def processar_arquivos(pastas):
    for caminho_arquivo in caminho_downloads.iterdir():
        # Verificando se é um arquivo (e não uma pasta)
        if caminho_arquivo.is_file():
            # Obtendo a extensão do arquivo
            extensao = caminho_arquivo.suffix

            # Tentando encontrar a pasta correspondente para a extensão
            for nome_pasta, extensoes in pastas.items():
                if extensao.lower() in extensoes:
                    destino = caminho_downloads / nome_pasta

                    # Criando a pasta de destino sob demanda
                    criar_pasta(destino)

                    # Movendo o arquivo para a pasta de destino
                    mover_arquivo(caminho_arquivo, destino)
                    break # Saindo do loop, já que encontramos a pasta correta e movemos o arquivo

# Função principal
def main():
    configurar_logger() # Configura o logger
    configuracoes = carregar_configuracoes() # Carrega as configurações do arquivo JSON
    pastas = configuracoes.get('pastas', {}) # Obtém o dicionário de pastas
    processar_arquivos(pastas) # Processa os arquivos no diretório de downloads

if __name__ == '__main__':
    main()
