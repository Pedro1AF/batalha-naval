import random

navioAbatidoJ = 0
navioAbatidoC = 0


def criar_tabuleiro(tamanho=10):
    return [["🌊" for _ in range(tamanho)] for _ in range(tamanho)]


tabuleiroJ = criar_tabuleiro()
tabuleiroC = criar_tabuleiro()

marJogador = criar_tabuleiro()
marComputador = criar_tabuleiro()


def exibirTab(tab):
    print("    " + " ".join(f"{i:2}" for i in range(1, 11)))
    for linha in range(10):
        print(f"{linha + 1:2} |", end=" ")
        for coluna in range(10):
            print(tab[linha][coluna], end=" ")
        print()
    print()


def posicionarFrotaJ():
    print("Jogador, escolha as posições das 5 embarcações!")

    navios = 0
    while navios < 5:
        linha = input(f"Navio {navios + 1} - Coordenada X (1-10): ")
        coluna = input(f"Navio {navios + 1} - Coordenada Y (1-10): ")

        if not (linha.isdigit() and coluna.isdigit()):
            print("Digite apenas números.")
            continue

        linha = int(linha)
        coluna = int(coluna)

        if not (1 <= linha <= 10 and 1 <= coluna <= 10):
            print("Coordenadas fora do tabuleiro.")
            continue

        linha -= 1
        coluna -= 1

        if marJogador[linha][coluna] != "🌊":
            print("Já existe um navio nessa posição.")
            continue

        marJogador[linha][coluna] = "🛥️ "
        navios += 1

        print(f"Restam {5 - navios} embarcações.\n")


def posicionarNavioC():
    navios = 0

    while navios < 5:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        if marComputador[linha][coluna] == "🌊":
            marComputador[linha][coluna] = "🛥️ "
            navios += 1


def disparoJ(x, y):
    global navioAbatidoJ

    mensagens = [
        "Seu tiro caiu na água!",
        "Nada além de ondas nesse local.",
        "Você acertou apenas alguns peixes.",
        "Tiro desperdiçado!",
        "Nenhum navio encontrado."
    ]

    if marComputador[x][y] == "🛥️ ":
        print("Parabéns! Você acertou um navio!")
        marComputador[x][y] = "X"
        tabuleiroC[x][y] = "X"
        navioAbatidoJ += 1

    elif marComputador[x][y] == "X":
        print("Você já atingiu essa posição.")

    elif marComputador[x][y] == "O":
        print("Você já atirou aqui.")

    else:
        marComputador[x][y] = "O"
        tabuleiroC[x][y] = "O"
        print(random.choice(mensagens))


def disparoC(x, y):
    global navioAbatidoC

    if marJogador[x][y] == "🛥️ ":
        print("O computador acertou um de seus navios!")
        marJogador[x][y] = "X"
        navioAbatidoC += 1

    elif marJogador[x][y] in ("X", "O"):
        return

    else:
        marJogador[x][y] = "O"
        print("O computador errou o disparo.")


print("\nTABULEIRO DO JOGADOR")
exibirTab(tabuleiroJ)

print("Posicionando frota do jogador...\n")
posicionarFrotaJ()

print("\nPosicionando frota do computador...\n")
posicionarNavioC()

print("\nSua frota:")
exibirTab(marJogador)

while True:

    print("\nTABULEIRO INIMIGO")
    exibirTab(tabuleiroC)

    while True:
        colunaX = input("Coordenada X do disparo (1-10): ")
        linhaY = input("Coordenada Y do disparo (1-10): ")

        if colunaX.isdigit() and linhaY.isdigit():
            numX = int(colunaX) - 1
            numY = int(linhaY) - 1

            if 0 <= numX <= 9 and 0 <= numY <= 9:
                disparoJ(numX, numY)
                break

        print("Entrada inválida.")

    print("\nComputador disparando...")

    while True:
        xComp = random.randint(0, 9)
        yComp = random.randint(0, 9)

        if marJogador[xComp][yComp] not in ("X", "O"):
            disparoC(xComp, yComp)
            break

    print("\nSua frota atual:")
    exibirTab(marJogador)

    if navioAbatidoJ >= 5:
        print("Parabéns! Você venceu a batalha naval!")
        print("Jogo desenvolvido por: Guilherme Guimarães, Felipe Eiki, Pedro Augusto")
        break

    if navioAbatidoC >= 5:
        print("O computador venceu a batalha naval!")
        print("Jogo desenvolvido por: Guilherme Guimarães, Felipe Eiki, Pedro Augusto")
        break
