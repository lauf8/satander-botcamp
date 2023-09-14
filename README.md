# Esportes de Inverno
Esse projeto tem como objetivo de consolidar em código o conhecimento em ETL do Bootcamp da Satander.

Eu fiz um sistema web usando o [Django](https://docs.djangoproject.com/en/4.2/) que é um framework web de Python, para ler e mostrar alguns dados que eu achei relevantes de cada esporte dos jogos olímpicos.

Para roda o projeto você deve ter o Python instalado em sua máquina e criar uma máquina virtual para esse projeto ser rodado, você pode instar o django e as outras libs Python diretamente em sua máquina
mas essa não é uma boa prática.

Você vai ter mais informações sobre máquinas virutais Python [aqui](https://docs.python.org/pt-br/3/library/venv.html).

Após fazer a instalação e ativar sua Vitualenv insira o comando 

```
pip install -r requirements.txt
```


Dentro do repositório tem o arquivo que eu faço a extração dos dados, é o arquivo sampledatawinterathletes.xlsx. Dentro dessa planilha tem os seguintes dados.

|Name |Sport |Nationality |Age |Wt |kg |Ht|
| -------- | ------- |  ------- | ------- | ------- | ------- | ------- |

Eu fiz uma tela para inserção dos dados:
![GitHub Logo](https://github.com/lauf8/satander-botcamp/blob/main/static/readme_img/fichario.png
)

Existe uma tela que lista todos os atletas:
![GitHub Logo](https://github.com/lauf8/satander-botcamp/blob/main/static/readme_img/atletas.png
)

Existe uma tela que lista todos as modalidades:
![GitHub Logo](https://github.com/lauf8/satander-botcamp/blob/main/static/readme_img/sports.png
)

E a tela final é uma tela detalhando todas as modalidades e com alguns KPI, indicando algumas informações que podem ser relevantes de cada  modalidade, como média de peso, idade, número de atletas inscritos e número de nações inscritas. 

Existe uma tela que lista todos as modalidades:
![GitHub Logo](https://github.com/lauf8/satander-botcamp/blob/main/static/readme_img/sports_detail.png
)
