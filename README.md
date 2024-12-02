# Lapyrinth

**Número da Lista**: 31<br>
**Conteúdo da Disciplina**: Grafos2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 21/061850  |  Henrique Azevedo Batalha |

## Sobre 
O projeto é um pequeno jogo criado utilizando a biblioteca pygame da linguagem python. Neste jogo o player (jogador) será colocado em um mapa (grafo) e o seu objetivo é fugir de um inimigo que o persegue utilizando o algorítimo de Dijkstra para determinar o seus movimentos.

## Screenshots

![screenshot1](https://github.com/projeto-de-algoritmos-2024/Grafos2_Lapyrinth/blob/master/screenshots/lapyrinth.png)

![screenshot2](https://github.com/projeto-de-algoritmos-2024/Grafos2_Lapyrinth/blob/master/screenshots/gameover.png)

![screenshot3](https://github.com/projeto-de-algoritmos-2024/Grafos2_Lapyrinth/blob/master/screenshots/mapa.jpg)

## Instalação 
**Linguagem**: Python<br>

Pré-requisitos: 

- Python3
- Pygame

**1:**
```
git clone https://github.com/projeto-de-algoritmos-2024/Grafos2_Lapyrinth.git
```

**2:**
```
pip install pygame
```

**3:**
```
python3 game.py
```
Também é possível rodar o projeto acessando o ambiente virtual da seguinte forma:
```
source venv/bin/activate
```

## Uso 
O jogador, representado pelo círculo amarelo, pode se mover com as setas direcionais do teclado ou apertar 'barra de espaço' para pular um movimento. Após 5 movimento o inimigo, representado pelo círculo vermelho, usa o algorítimo de Dijkstra para traçar um caminho até o jogador, o inimigo possui a limitação de 5 de custo das arestas. A diferença entre a movimentação dos dois é que na movimentação do jogador, o peso das arestas não é considerado.

### Comandos Adicionais:

A tecla 'd' executa o algorítimo de Dijkstra, printando a lista de distancias no terminal

A tecla 'esc" fecha o jogo

## Apresentação

**Link do vídeo**

[![Assista ao vídeo](https://img.youtube.com/vi/kt3zuHldwyI/0.jpg)](https://www.youtube.com/watch?v=kt3zuHldwyI)

https://www.youtube.com/watch?v=kt3zuHldwyI




