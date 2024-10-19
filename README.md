# Projeto: Pacote de Processamento de Imagens
O objetivo do projeto além de empacotar com packages e modulos é realizar a combinação e compartação de imagens.

#### Tecnologia: Python 3.12.2
#### Data: 19/10/2024
-----------------------------------------
### Descrição
O pacote "EDimageProcessing" é usado para:

- Módulo "Processing":
  - Correspondência de histograma;
  - Similaridade estrutural;
  - Redimensionar imagem;

- Módulo "Utils":
  - Ler imagem;
  - Salvar imagem;
  - Plotar imagem;
  - Resultado do gráfico;
  - Plotar histograma;
---------------------------------------------
## Passo a passo da configuração para hospedar um pacote em Python no ambiente de testes Test Pypi

- [x] Instalação das últimas versões de "setuptools" e "wheel"

```
py -m pip install --user --upgrade setuptools wheel
```
- [x] Tenha certeza que o diretório no terminal seja o mesmo do arquivo "setup.py"

```
image-processing-package py setup.py sdist bdist_wheel
```

- [x] Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:
  - [x] build;
  - [x] dist;
  - [x] edimageprocessing.egg-info.

- [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository testpypi dist/*
```

- [x] Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.

### Este projeto é inpirado no de https://www.linkedin.com/in/karinakato/, que estou usando para testar o Test Pypi, esse código foi passado como aula na plataforma DIO.me sendo necessário seu envio para concluir um curso. Este arquivo .md foi inspirado no do https://github.com/andremrezende/python-packages/blob/main/README.md?plain=1 .

### No entanto, tenha em mente que o Test Pypi, como o próprio nome diz, é apenas um ambiente de testes. Para que o projeto esteja disponível como um pacote para ser usado publicamente, é necessário hospedá-lo no site oficial do Pypi.
----------------------------------------------------
## Instalação local, após hospedagem no Test Pypi

- [x] Instalação de dependências
```
pip install -r requirements.txt
```

- [x] Instalção do Pacote

Use o gerenciador de pacotes ```pip install -i https://test.pypi.org/simple/ edimageprocessing ```para instalar EDimageProcessing

```bash
pip install edimageprocessing
```
-------------------------------------------------
## Como usar em qualquer projeto

```python
from edimageprocessing.processing import combination
combination.find_difference(image1, image2)
```

## Autor (Quem hospedou o projeto no Test Pypi)
Eduardo Santos

https://choosealicense.com/licenses/mit/