# Organizador da Pasta de Downloads

Este script Python visa automatizar a organização de arquivos baixados na pasta de Downloads do Windows, com base em configurações definidas em um arquivo JSON.

## Funcionamento

O script lê um arquivo JSON de configuração (`configuracoes.json`) que define para quais tipos de arquivos cada pasta deve ser utilizada. Após a leitura das configurações, ele verifica os arquivos na pasta de Downloads do usuário e os move para suas respectivas pastas, de acordo com a extensão do arquivo.

## Pré-requisitos

Antes de executar o script, certifique-se de que o arquivo de configuração `configuracoes.json` está presente no mesmo diretório do script. Este arquivo deve ser inicialmente copiado do modelo `configuracoes-exemplo.json` e personalizado conforme necessário.

## Como Usar

1. Clone o repositório e navegue até o diretório do projeto:
    ```
    git clone https://github.com/luizelias8/organizador-pasta-downloads.git
    cd organizador-pasta-downloads
    ```

2. Preparação:
- Copie o arquivo `configuracoes-exemplo.json` para `configuracoes.json`.
- Personalize as configurações em `configuracoes.json` de acordo com suas preferências.

3. Execução:
- Execute o script Python.
- Os arquivos da pasta de Downloads serão automaticamente movidos para as pastas correspondentes conforme as extensões definidas no arquivo `configuracoes.json`.

## Observações
- Se algum arquivo não puder ser movido devido a permissões insuficientes ou por estar em uso, o script informará o problema para aquele arquivo específico.

## Dica: Agendamento Automático no Windows

Para garantir que a organização automática de downloads seja executada regularmente, você pode configurar o Agendador de Tarefas do Windows para rodar o script em intervalos específicos ou em horários definidos.

## Contribuição

Contribuições são bem-vindas!

## Autor

- [Luiz Elias](https://github.com/luizelias8)