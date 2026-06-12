import random
navioAbatidoJ = 0
navioAbatidoC = 0
#Abaixo são todas as funções do jogo
#-------
#funçao que cria um tabuleiro para o Jogador de tamanho 10x10
def tabuleiroJog(tamanho):
    tabuleiroJ = []
    for casa in range(tamanho):
        tabuleiroJ.append(["🌊"] * tamanho)
    return tabuleiroJ
tabuleiroJ = tabuleiroJog(10)
#-------
#funçao que cria um tabuleiro para o Computador de tamanho 10x10
def tabuleiroComp(tamanho):
    tabuleiroC = []
    for i in range(tamanho):
        tabuleiroC.append(["🌊"] * tamanho)
    return tabuleiroC
tabuleiroC = tabuleiroComp(10)
#-------
#esta função é para o tabuleiro do jogador onde ficara sua frota oculta
def frotaJ(mar):
    naviosJ = []
    for i in range(mar):
        naviosJ.append(["🌊"] * mar)
    return naviosJ
marJogador = frotaJ(10)
#-------
#esta função é para o tabuleiro do computador onde ficara sua frota oculta
def frotaC(mar):
    naviosC = []
    for i in range(mar):
        naviosC.append(["🌊"] * mar)
    return naviosC
marComputador = frotaC(10)
#-------
#Abaixo são as duas funçoes para exibir os tabuleiros com as cordenadas das linhas e colunas respectivas
def exibirTabJogador(tabJ):
    print("\nTabuleiro Jogador\n")
    for linha in range(11):
        if linha == 0:
            print(f"  X\nY .{1:2}", end="| ")
            for col1 in range(2, 11):
                print(f"{col1:1}|", end=" ")
        else:
            print(f"{linha:2}", end=" ")
            for coluna in range(10):
                print(tabJ[linha - 1][coluna], end=" ")
        print()
#-------
def exibirTabComp(tabC):
    print("\nTabuleiro Computador\n")
    for linha in range(11):
        if linha == 0:
            print(f"  X\nY .{1:2}", end="| ")
            for col1 in range(2, 11):
                print(f"{col1:1}|", end=" ")
        else:
            print(f"{linha:2}", end=" ")
            for coluna in range(10):
                print(tabuleiroC[linha - 1][coluna], end=" ")
        print()
#-------
#Agora aqui abaixo é o momento de escolha das posições das embarcações
#-------
#Primeiramente o jogador decide suas posições
def posicionarFrotaJ():
   print("Jogador escolha as posições em que deseja alocar suas embarcaçoes!")
   qntdNavio = 0
   while True:
        while True:
            linha = input("Selecione a cordenada X em que deseja adicionar uma embarcação: ")
            coluna = input("Agora o valor da cordenada Y desejada: ")
            if linha.isdigit() and coluna.isdigit():
                numlinha = int(linha)
                numcoluna = int(coluna)
                break
            else:
                print("Entrada inválida. Por favor, digite apenas números.")
        formL = numlinha - 1
        formC = numcoluna - 1
        if numlinha <= 10 and numcoluna <= 10:
            if marJogador[formL][formC] == "🌊":
                marJogador[formL][formC] = "🛥️ "
            else:
                print("As cordenadas escolhidas ja estão ocupadas por outra embarcação" \
                "por favor escolha outra")
                qntdNavio -= 1
        else:
            print("As cordenadas escolhidas estão fora do alcance do tabuleiro" \
            "por favor escolha outra posição")
            qntdNavio -= 1

        qntdRest = 4 - qntdNavio
        qntdNavio += 1

        if qntdNavio != 5:
            print(f"Ainda restam {qntdRest} embarcações a serem posicionadas")
        else:
            print("Todas as embarcações foram alocadas, se prerare para a batalha!")
            break
#-------
print("O computador vai escolher as posições que deseja agora!")
##-------
##Agora o momento da maquina escolhes as suas posiçoes
def poscionarNavioC():
   for i in range(0, 5):
       linhaComp = random.randint(0, 9)
       colunaComp = random.randint(0, 9)
       if marComputador[linhaComp][colunaComp] == "🌊":
           marComputador[linhaComp][colunaComp] = "🛥️ "
       else:
           i -= 1
#-------
#Nesta seção está o codígo onde os disparos vao ser realizados pelos jogadores
def disparoJ(X, Y):
    erroJogador = ["Seu tiro caiu na água!","Nada além de ondas nesse local.","Você acertou apenas alguns peixes.",
    "O oceano agradece pela nova cratera.","Tiro desperdiçado! Nenhum navio encontrado.",
    "As gaivotas ficaram assustadas, mas os navios não.","Água por todos os lados!",
    "Seu projétil desapareceu nas profundezas do mar.","Nenhuma embarcação foi atingida.", 
    "O radar deve estar com defeito, tiro na água!"]
    mensagemErro = random.choice(erroJogador)
    if marComputador[X][Y] == "🛥️ ":
        print("Parabens Jogador você atingiu o alvo!")
        navioAbatidoJ += 1
    else:
        print(mensagemErro)
#-------
def disparoC(X, Y):
    erroComputador = ["O computador atirou longe do alvo.","Os sistemas inimigos falharam na mira.","Tiro inimigo na água!",
    "O computador não encontrou sua frota.","As embarcações permanecem seguras.","A inteligência artificial calculou errado.",
    "O inimigo desperdiçou munição.", "Nenhum dano causado à sua frota.","Os navios escaparam por pouco.",
    "O computador precisa recalibrar seus sensores."]
    erroComp = random.choice(erroComputador)
    if marJogador[X][Y] == "🛥️ ":
        print("O computador acertou em cheio")
        navioAbatidoC += 1
    else:
        print(erroComp)
#-------



print(exibirTabJogador(tabuleiroJ))
posicionarFrotaJ()
print("Agora observe como suas tropas ficaram alocadas no mar")
print(exibirTabJogador(marJogador))

while True:
    print("Jogador agora voce vai realizar o disparo")
    colunaX = int(input("Insira a cordenada X que deseja realizar o disparo: "))
    linhaY = int(input("Insira a cordenada Y que deseja realizar o disparo: "))
    cordenada = colunaX, linhaY
    localAcerto = disparoJ(cordenada)
    print(localAcerto)
    #-------
    print("Agora o computador vai realizar o disparo!")
    escolhaXComp = random.randint(0, 9)
    escolhaYComp = random.randint(0, 9)
    disparoC(escolhaXComp, escolhaYComp)
    if navioAbatidoJ == 5:
        print("Parabens jogador voce ganhou o jogo!")
        break
    elif navioAbatidoC == 5:
        print("O computador ganhou!")
        break
    else:
        pass
