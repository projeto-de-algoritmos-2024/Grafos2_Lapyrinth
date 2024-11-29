import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Constantes de configuração
screen_width = 1000
screen_height = 800
TAMANHO_NO = 20

# Configurar a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Labirinto")

# Definir cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)

# Classe para o grafo
class Grafo:
    def __init__(self):
        self.nos = {}
    
    def adicionar_no(self, nome, posicao):
        self.nos[nome] = {'posicao': posicao, 'arestas': []} # posicao = [x, y], arestas = lista de nos conectados
    
    def adicionar_aresta(self, no1, no2): # Adiciona em arestas ["no1", "no2"] que estao conectados
        self.nos[no1]['arestas'].append(no2)
        self.nos[no2]['arestas'].append(no1)
    
    def get_posicao(self, no): # Retorna pos do no
        return self.nos[no]['posicao']
    
    def get_arestas(self, no): # REtorna pos aresta do no
        return self.nos[no]['arestas']

# Classe do Personagem
class Player:
    def __init__(self, grafo, no_inicial): # Recebe grafo e no inical
        self.grafo = grafo
        self.no_atual = no_inicial
        self.posicao = grafo.get_posicao(no_inicial)
    
    def mover(self, direção):
        arestas = self.grafo.get_arestas(self.no_atual)
        if direção in arestas: # Se direcao da aresta esta conectada
            self.no_atual = direção
            self.posicao = self.grafo.get_posicao(direção) # Atualiza posicao

# Inicia o grafo
grafo = Grafo()

# Definir nos -> Nome do no, POS X, POS Y
BordaX = 50
BordaY = 50
grafo.adicionar_no("A0", (BordaX, BordaY))
grafo.adicionar_no("A1", (BordaX, BordaY + 100))
grafo.adicionar_no("A2", (BordaX, BordaY + 200))
grafo.adicionar_no("C0", (BordaX + 100, BordaY))
grafo.adicionar_no("C1", (BordaX + 100, BordaY + 100))
grafo.adicionar_no("C2", (BordaX + 100, BordaY + 200))
grafo.adicionar_no("D1", (BordaX + 200, BordaY + 100))
grafo.adicionar_no("D2", (BordaX + 200, BordaY + 200))
grafo.adicionar_no("E0", (BordaX + 300, BordaY))
grafo.adicionar_no("E1", (BordaX + 300, BordaY + 100))
grafo.adicionar_no("E2", (BordaX + 300, BordaY + 200))
grafo.adicionar_no("E3", (BordaX + 300, BordaY + 300))

# Definir arestas -> No -> No 
grafo.adicionar_aresta("A0", "C0")
grafo.adicionar_aresta("A0", "A1")
grafo.adicionar_aresta("A1", "C1")
grafo.adicionar_aresta("A1", "A2")
grafo.adicionar_aresta("A2", "C2")
grafo.adicionar_aresta("C0", "E0")
grafo.adicionar_aresta("C0", "C1")
grafo.adicionar_aresta("C1", "D1")
grafo.adicionar_aresta("C1", "C2")
grafo.adicionar_aresta("D1", "E1")
grafo.adicionar_aresta("D1", "D2")
grafo.adicionar_aresta("D2", "E2")
grafo.adicionar_aresta("E0", "E1")

# Coloca player
player = Player(grafo, "A0")

# Funcao para desenhar o grafo na tela
def desenhar_mapa():
    for no, dados in grafo.nos.items():
        x, y = dados['posicao'] # Pega as coordenadas do no
        pygame.draw.circle(screen, AZUL, (x, y), TAMANHO_NO) # Desenha o no
        for vizinho in dados['arestas']: 
            x2, y2 = grafo.get_posicao(vizinho) # Pega as arestas do no
            pygame.draw.line(screen, BRANCO, (x, y), (x2, y2), 3) # Desenha as arestas do no

# Funcao para desenhar o player
def desenhar_player():
    pygame.draw.circle(screen, AMARELO, player.posicao, TAMANHO_NO // 2) # Faz ele um pouc menor que o no

# Funcao principal do jogo
def game_loop():
    running = True
    while running:
        screen.fill(PRETO) # pinta o fundo
        desenhar_mapa()
        desenhar_player()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: # Usuario aperta alguma tecla
                if event.key == pygame.K_UP: # Apertou cima
                    for vizinho in grafo.get_arestas(player.no_atual):
                        if grafo.get_posicao(vizinho)[1] < player.posicao[1]: # Se Y do vizinho for menor, entao vizinho esta em cima
                            player.mover(vizinho)
                            break
                elif event.key == pygame.K_DOWN:  # Apertou baixo
                    for vizinho in grafo.get_arestas(player.no_atual):
                        if grafo.get_posicao(vizinho)[1] > player.posicao[1]: # Se Y do vizinho for maior, entao vizinho esta em baixo
                            player.mover(vizinho)
                            break
                elif event.key == pygame.K_RIGHT:  # Apertou direita
                    for vizinho in grafo.get_arestas(player.no_atual):
                        if grafo.get_posicao(vizinho)[0] > player.posicao[0]: # Se X do vizinho for maior, entao vizinho esta a direita
                            player.mover(vizinho)
                            break
                elif event.key == pygame.K_LEFT: #  # Apertou esquerda
                    for vizinho in grafo.get_arestas(player.no_atual): # Se X do vizinho for menor, entao vizinho esta a esquerda
                        if grafo.get_posicao(vizinho)[0] < player.posicao[0]:
                            player.mover(vizinho)
                            break
                elif event.key == pygame.K_ESCAPE: # Apertou Esc
                    pygame.quit() #Fecha jogo e programa
                    sys.exit()
        
        pygame.display.flip()

game_loop()
