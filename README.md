# Análise de Imagens com Flask e Transformadores

Este projeto é uma aplicação web para análise de imagens, onde o backend utiliza um modelo de processamento de linguagem natural para gerar descrições em inglês e traduzi-las para o português. O frontend permite aos usuários enviar imagens para análise e exibir a descrição gerada.

## Estrutura do Projeto

O projeto é dividido em duas partes principais:

- **Backend**: Construído com Flask, utiliza o modelo BLIP da biblioteca `transformers` para gerar descrições de imagens e traduzir essas descrições para português usando `googletrans`.
- **Frontend**: Construído com HTML, CSS e JavaScript, permite aos usuários enviar imagens e ver o resultado da análise.

## Requisitos

- Python 3.7+
- pip

## Principais Bibliotecas Utilizadas

- **Flask**
- **transformers**
- **Pillow**
- **googletrans**
- **Flask-CORS**

## Configuração e Instalação

- git clone https://github.com/kaiquedu/analisar-imagem-app.git
- cd analisar-imagem-app
- Use o script run.bat ou bash run.sh para iniciar a aplicação
