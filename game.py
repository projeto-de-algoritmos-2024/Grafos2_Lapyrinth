import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Constantes de configuração
screen_width = 1200
screen_height = 900
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
VERMELHO = (255, 0, 0)

# Classe para o grafo
class Grafo:
    def __init__(self):
        self.nos = {}
    
    def adicionar_no(self, nome, posicao):
        self.nos[nome] = {'posicao': posicao, 'arestas': []} # posicao = [x, y], arestas = lista de nos conectados
    
    def adicionar_aresta(self, no1, no2, peso): # Adiciona em arestas ["no1", "no2"] que estao conectados
        self.nos[no1]['arestas'].append((no2, peso))
        self.nos[no2]['arestas'].append((no1, peso))
    
    def get_posicao(self, no): # Retorna pos do no
        return self.nos[no]['posicao']
    
    def get_arestas(self, no): # REtorna pos aresta do no
        #return self.nos[no]['arestas']
        return [vizinho for vizinho, peso in self.nos[no]['arestas']] # Retorna apenas as arestas 
    
    def get_arestasPeso(self, no): # REtorna pos aresta do no (Com peso)
        return self.nos[no]['arestas']

# Classe do Personagem
class Player:
    def __init__(self, grafo, no_inicial): # Recebe grafo e no inical
        self.grafo = grafo
        self.no_atual = no_inicial # Guarda no atual
        self.posicao = grafo.get_posicao(no_inicial)
    
    def mover(self, direção):
        arestas = self.grafo.get_arestas(self.no_atual)
        if direção in arestas: # Se direcao da aresta esta conectada
            self.no_atual = direção # Guarda as coordenadas [X,Y] atuais
            self.posicao = self.grafo.get_posicao(direção) # Atualiza posicao

# Classe do Inimigo
class Inimigo:
    def __init__(self, grafo, no_inicial): # Recebe grafo e no inical
        self.grafo = grafo
        self.no_atual = no_inicial # Guarda no atual
        self.posicao = grafo.get_posicao(no_inicial) # Guarda as coordenadas [X,Y] atuais
    
    def mover(self, direção): 
        arestas = self.grafo.get_arestas(self.no_atual)
        if direção in arestas: # Se direcao da aresta esta conectada
            self.no_atual = direção
            self.posicao = self.grafo.get_posicao(direção) # Atualiza posicao

    def dijkstra(self, destino): 
        distancias = {no: sys.maxsize for no in self.grafo.nos} # Inicializa distancias com "infito"
        distancias[self.no_atual] = 0 # Coloca o no inicial como 0
        
        nos_pendentes = [(0, self.no_atual)]  # (distancia, no)
        visitados = set()  # Conjunto de nos visitados
        caminhos = {self.no_atual: []}  # Armazena o caminho ate cada no

        while nos_pendentes:
            nos_pendentes.sort()  # Ordena nos peor menor distancia
            distancia_atual, vertice_atual = nos_pendentes.pop(0) # Remove

            if vertice_atual in visitados: # Continua caso no ja visitado
                continue

            visitados.add(vertice_atual) # Marca como visitado

            if vertice_atual == destino: # Interrompe caso ache o player
                break  
            
            for vizinho, peso in self.grafo.get_arestasPeso(vertice_atual):  # Atualiza distancias dos vizinhos
                nova_distancia = distancias[vertice_atual] + peso  # Soma o peso da aresta
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    nos_pendentes.append((distancias[vizinho], vizinho))
                    caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]  # Armazena o caminho ate o vizinho

        return caminhos, distancias # Retorna as distancias mais curtas ate o destino

# Inicia o grafo
grafo = Grafo()

# Definir nos -> Nome do no, POS X, POS Y
BordaX = 50
BordaY = 50
grafo.adicionar_no("A0", (BordaX, BordaY))
grafo.adicionar_no("A1", (BordaX, BordaY + 100))
grafo.adicionar_no("A2", (BordaX, BordaY + 200))
grafo.adicionar_no("A6", (BordaX, BordaY + 600))
grafo.adicionar_no("A8", (BordaX, BordaY + 800))
grafo.adicionar_no("C0", (BordaX + 100, BordaY))
grafo.adicionar_no("C1", (BordaX + 100, BordaY + 100))
grafo.adicionar_no("C2", (BordaX + 100, BordaY + 200))
grafo.adicionar_no("C4", (BordaX + 100, BordaY + 400))
grafo.adicionar_no("C6", (BordaX + 100, BordaY + 600))
grafo.adicionar_no("C7", (BordaX + 100, BordaY + 700))
grafo.adicionar_no("C8", (BordaX + 100, BordaY + 800))
grafo.adicionar_no("D1", (BordaX + 200, BordaY + 100))
grafo.adicionar_no("D2", (BordaX + 200, BordaY + 200))
grafo.adicionar_no("D3", (BordaX + 200, BordaY + 300))
grafo.adicionar_no("D4", (BordaX + 200, BordaY + 400))
grafo.adicionar_no("D5", (BordaX + 200, BordaY + 500))
grafo.adicionar_no("D6", (BordaX + 200, BordaY + 600))
grafo.adicionar_no("D7", (BordaX + 200, BordaY + 700))
grafo.adicionar_no("E0", (BordaX + 300, BordaY))
grafo.adicionar_no("E1", (BordaX + 300, BordaY + 100))
grafo.adicionar_no("E2", (BordaX + 300, BordaY + 200))
grafo.adicionar_no("E3", (BordaX + 300, BordaY + 300))
grafo.adicionar_no("E6", (BordaX + 300, BordaY + 600))
grafo.adicionar_no("E7", (BordaX + 300, BordaY + 700))
grafo.adicionar_no("F3", (BordaX + 400, BordaY + 300))
grafo.adicionar_no("F4", (BordaX + 400, BordaY + 400))
grafo.adicionar_no("F7", (BordaX + 400, BordaY + 700))
grafo.adicionar_no("G1", (BordaX + 500, BordaY + 100))
grafo.adicionar_no("G3", (BordaX + 500, BordaY + 300))
grafo.adicionar_no("G4", (BordaX + 500, BordaY + 400))
grafo.adicionar_no("G5", (BordaX + 500, BordaY + 500))
grafo.adicionar_no("G6", (BordaX + 500, BordaY + 600))
grafo.adicionar_no("G8", (BordaX + 500, BordaY + 800))
grafo.adicionar_no("H1", (BordaX + 600, BordaY + 100))
grafo.adicionar_no("H2", (BordaX + 600, BordaY + 200))
grafo.adicionar_no("H3", (BordaX + 600, BordaY + 300))
grafo.adicionar_no("H4", (BordaX + 600, BordaY + 400))
grafo.adicionar_no("H5", (BordaX + 600, BordaY + 500))
grafo.adicionar_no("H6", (BordaX + 600, BordaY + 600))
grafo.adicionar_no("H7", (BordaX + 600, BordaY + 700))
grafo.adicionar_no("I0", (BordaX + 700, BordaY ))
grafo.adicionar_no("I1", (BordaX + 700, BordaY + 100 ))
grafo.adicionar_no("I3", (BordaX + 700, BordaY + 300 ))
grafo.adicionar_no("I5", (BordaX + 700, BordaY + 500 ))
grafo.adicionar_no("I6", (BordaX + 700, BordaY + 600 ))
grafo.adicionar_no("I7", (BordaX + 700, BordaY + 700 ))
grafo.adicionar_no("J0", (BordaX + 800, BordaY ))
grafo.adicionar_no("J1", (BordaX + 800, BordaY + 100 ))
grafo.adicionar_no("J2", (BordaX + 800, BordaY + 200 ))
grafo.adicionar_no("J3", (BordaX + 800, BordaY + 300 ))
grafo.adicionar_no("J6", (BordaX + 800, BordaY + 600 ))
grafo.adicionar_no("J7", (BordaX + 800, BordaY + 700 ))
grafo.adicionar_no("J8", (BordaX + 800, BordaY + 800 ))

# Definir arestas -> No <-> No , peso
grafo.adicionar_aresta("A0", "C0", 1)
grafo.adicionar_aresta("A0", "A1", 1)
grafo.adicionar_aresta("A1", "C1", 1)
grafo.adicionar_aresta("A1", "A2", 1)
grafo.adicionar_aresta("A2", "C2", 1)
grafo.adicionar_aresta("A6", "C6", 1)
grafo.adicionar_aresta("A6", "A8", 2)
grafo.adicionar_aresta("A8", "C8", 1)
grafo.adicionar_aresta("C0", "E0", 2)
grafo.adicionar_aresta("C0", "C1", 1)
grafo.adicionar_aresta("C1", "D1", 1)
grafo.adicionar_aresta("C1", "C2", 1)
grafo.adicionar_aresta("C2", "C4", 2)
grafo.adicionar_aresta("C4", "C6", 2)
grafo.adicionar_aresta("C6", "D6", 1)
grafo.adicionar_aresta("C7", "C8", 1)
grafo.adicionar_aresta("C7", "D7", 1)
grafo.adicionar_aresta("D1", "E1", 1)
grafo.adicionar_aresta("D1", "D2", 1)
grafo.adicionar_aresta("D2", "E2", 1)
grafo.adicionar_aresta("D3", "E3", 1)
grafo.adicionar_aresta("D3", "D4", 1)
grafo.adicionar_aresta("D4", "F4", 2)
grafo.adicionar_aresta("D5", "D6", 1)
grafo.adicionar_aresta("D5", "G5", 3)
grafo.adicionar_aresta("D6", "E6", 1)
grafo.adicionar_aresta("D7", "E7", 1)
grafo.adicionar_aresta("E0", "E1", 1)
grafo.adicionar_aresta("E1", "G1", 2)
grafo.adicionar_aresta("E2", "E3", 1)
grafo.adicionar_aresta("E3", "E6", 3)
grafo.adicionar_aresta("E3", "F3", 1)
grafo.adicionar_aresta("E7", "F7", 1)
grafo.adicionar_aresta("F3", "G3", 1)
grafo.adicionar_aresta("F7", "H7", 2)
grafo.adicionar_aresta("G1", "H1", 1)
grafo.adicionar_aresta("G3", "G4", 1)
grafo.adicionar_aresta("G3", "H3", 1)
grafo.adicionar_aresta("G4", "H4", 1)
grafo.adicionar_aresta("G5", "H5", 1)
grafo.adicionar_aresta("G6", "H6", 1)
grafo.adicionar_aresta("G6", "G8", 2)
grafo.adicionar_aresta("G8", "J8", 3)
grafo.adicionar_aresta("H1", "I1", 1)
grafo.adicionar_aresta("H1", "H2", 1)
grafo.adicionar_aresta("H2", "J2", 2)
grafo.adicionar_aresta("H3", "H4", 1)
grafo.adicionar_aresta("H5", "H6", 1)
grafo.adicionar_aresta("H7", "I7", 1)
grafo.adicionar_aresta("F4", "F7", 3)
grafo.adicionar_aresta("I0", "I1", 1)
grafo.adicionar_aresta("I0", "J0", 1)
grafo.adicionar_aresta("I1", "J1", 1)
grafo.adicionar_aresta("I3", "J3", 1)
grafo.adicionar_aresta("I3", "I5", 2)
grafo.adicionar_aresta("I5", "I6", 1)
grafo.adicionar_aresta("I6", "J6", 1)
grafo.adicionar_aresta("I7", "J7", 1)
grafo.adicionar_aresta("J0", "J1", 1)
grafo.adicionar_aresta("J1", "J2", 1)
grafo.adicionar_aresta("J2", "J3", 1)
grafo.adicionar_aresta("J6", "J7", 1)
grafo.adicionar_aresta("J7", "J8", 1)

# Coloca player
player = Player(grafo, "A0")
# Coloca inimigo
inimigo = Inimigo(grafo, "H4")

# Funcao para desenhar o grafo na tela
def desenhar_mapa():
    for no, dados in grafo.nos.items():
        x, y = dados['posicao'] # Pega as coordenadas do no
        pygame.draw.circle(screen, AZUL, (x, y), TAMANHO_NO) # Desenha o no
        for vizinho, peso in dados['arestas']:
            x2, y2 = grafo.get_posicao(vizinho) # Pega as arestas do no
            pygame.draw.line(screen, BRANCO, (x, y), (x2, y2), 3) # Desenha as arestas do no

# Funcao para desenhar o player
def desenhar_player():
    pygame.draw.circle(screen, AMARELO, player.posicao, TAMANHO_NO // 2) # Faz ele um pouc menor que o no

# Funcao para desenhar o inimigo
def desenhar_inimigo():
    pygame.draw.circle(screen, VERMELHO, inimigo.posicao, TAMANHO_NO // 2) # Faz ele um pouc menor que o no

# Funcao para desenhar o gameover
def desenhar_gameover():
    font = pygame.font.Font('freesansbold.ttf', 50) # Seleciona a fonte 
    screen.fill(PRETO) # Pinta o fundo todo de preto
    text = font.render('GAMEOVER', True, PRETO, AZUL) # Escreve GAMEOVER em azul
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, textRect)

# Funcao para desenhar o contador de movimentos, turnos, posicao e linha lateral
def desenhar_contador(movimentos, player, turno):
    pygame.draw.line(screen, VERDE, (screen_width - 300, 0), (screen_width - 300, screen_height), 3) # Desenha linha lateral na tela
    font = pygame.font.Font('freesansbold.ttf', 12) # Seleciona a fonte 
    texto = 'Turno: {}'.format(turno)  # Formata string 
    text = font.render(texto, True, PRETO, VERDE)
    textRect = text.get_rect()
    textRect.center = (screen_width - 150, 10)
    screen.blit(text, textRect)

    texto = 'Movimentos: {}/5'.format(movimentos)  # Formata string 
    text = font.render(texto, True, PRETO, VERDE)
    textRect = text.get_rect()
    textRect.center = (screen_width - 150, 25)
    screen.blit(text, textRect)

    texto = 'Posição: {}'.format(player.no_atual)
    text = font.render(texto, True, PRETO, VERDE)
    textRect = text.get_rect()
    textRect.center = (screen_width - 150, 40)
    screen.blit(text, textRect)

def desenhar_dijkstra(distancias, caminho):
    font = pygame.font.Font('freesansbold.ttf', 12) # Seleciona a fonte 
    text = font.render('Caminho Inimigo -> Player:', True, PRETO, VERDE)
    textRect = text.get_rect()
    textRect.center = (screen_width - 150, 60)
    screen.blit(text, textRect)

    texto = '{}'.format(caminho)
    text = font.render(texto, True, PRETO, VERDE)
    textRect = text.get_rect()
    textRect.center = (screen_width - 150, 75)
    screen.blit(text, textRect)

# Funcao principal do jogo
def game_loop():
    running = True
    jogando = True # Determina se o jogo continua
    movimentos = 0 # Vai guardar o numero de casas andadas
    turno = 0
    distancias = None
    caminho = None

    while running: # Inicia o loop de jogo
        screen.fill(PRETO) # pinta o fundo
        desenhar_mapa()
        desenhar_player()
        desenhar_inimigo()
        desenhar_contador(movimentos, player, turno)
        desenhar_dijkstra(distancias, caminho)

        if movimentos == 5:
            movimentos = 0 # Reseta o contador de movimentos
            turno += 1
            caminhos, distancias = inimigo.dijkstra(player.no_atual)
    
            caminho = caminhos.get(player.no_atual, []) # Pega o caminho para o jogador
            peso_max = 5
            for no in caminho:
                proximo_peso = distancias.get(no)
                if proximo_peso <= peso_max:
                    inimigo.mover(no)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN: # Usuario aperta alguma tecla
                if event.key == pygame.K_UP and jogando: # Apertou cima
                    for vizinho in grafo.get_arestas(player.no_atual):
                        if grafo.get_posicao(vizinho)[1] < player.posicao[1]: # Se Y do vizinho for menor, entao vizinho esta em cima
                            movimentos +=1 # Incrementa o contador de movimentos
                            player.mover(vizinho)
                            break
                elif event.key == pygame.K_DOWN and jogando:  # Apertou baixo
                    for vizinho in grafo.get_arestas(player.no_atual):
                        if grafo.get_posicao(vizinho)[1] > player.posicao[1]: # Se Y do vizinho for maior, entao vizinho esta em baixo
                            player.mover(vizinho)
                            movimentos +=1 # Incrementa o contador de movimentos
                            break
                elif event.key == pygame.K_RIGHT and jogando:  # Apertou direita
                    for vizinho in grafo.get_arestas(player.no_atual):
                        if grafo.get_posicao(vizinho)[0] > player.posicao[0]: # Se X do vizinho for maior, entao vizinho esta a direita
                            player.mover(vizinho)
                            movimentos +=1 # Incrementa o contador de movimentos
                            break
                elif event.key == pygame.K_LEFT and jogando: #  # Apertou esquerda
                    for vizinho in grafo.get_arestas(player.no_atual): # Se X do vizinho for menor, entao vizinho esta a esquerda
                        if grafo.get_posicao(vizinho)[0] < player.posicao[0]:
                            player.mover(vizinho)
                            movimentos +=1 # Incrementa o contador de movimentos
                            break
                elif event.key == pygame.K_SPACE and jogando: # Apertou barra de espaco
                    movimentos +=1 # Apenas pula a vez
                    break
                elif event.key == pygame.K_ESCAPE: # Apertou Esc
                    pygame.quit() #Fecha jogo e programa
                    sys.exit()
                elif event.key == pygame.K_d: # Apertou d 
                    caminhos, distancias = inimigo.dijkstra(player.no_atual) # Executa dijkstra e printa o caminho no terminal
                    caminho = caminhos.get(player.no_atual, [])
                    print(distancias)
                    print(caminho)
                    

        if player.no_atual == inimigo.no_atual: # Quando o player encosta no inimigo
            jogando = False # Finaliza jogo
            desenhar_gameover()      
        
        pygame.display.flip()

game_loop()
