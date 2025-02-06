tabuleiro = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def exibir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        print(f' {linha[0] or " "} | {linha[1] or " "} | {linha[2] or " "}')

        if i < 2:
            print('-----------')

def fazer_jogada(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == '':
        tabuleiro[linha][coluna] = jogador
        return True
    return False

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
        
    for coluna in range(3):
        if [tabuleiro[i][coluna] for i in range(3)].count(jogador) == 3:
            return True
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

def jogar():
    tabuleiro = [['', '', ''] for _ in range(3)]
    jogador_atual = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)
        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))

        if fazer_jogada(tabuleiro, linha, coluna, jogador_atual):
            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} venceu!")
                break
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogar()