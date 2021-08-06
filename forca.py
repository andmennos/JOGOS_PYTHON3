import random

def jogar():
    imprime_mensagem_inicial()
    palavra_secreta = gera_palavra_secreta()
    letras_acertadas = imprime_espaco_palavra(palavra_secreta)
    letras_faltando = conta_letras(letras_acertadas)

    print(f"A palavra secreta possui {letras_faltando} letras.")
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = solicita_chute()

        if chute in palavra_secreta:
            adiciona_letra_acertada(palavra_secreta, chute, letras_acertadas)

        else:
            erros += 1
            desenha_forca(erros, letras_acertadas)

        acertou = verifica_se_ganhou(letras_acertadas)
        enforcou = verifica_se_perdeu(erros)

        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_inicial():
    print('**********************************')
    print('****Bem vindo ao Jogo da Forca****')
    print('**********************************')

def conta_letras(letras_acertadas):
    letras_faltando = str(letras_acertadas.count("_"))
    return letras_faltando

def gera_palavra_secreta():
    palavras = []
    with open("palavras_frutas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip().lower()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def imprime_espaco_palavra(palavra_secreta):
    letras_acertadas = ["_" for letra in palavra_secreta]
    return letras_acertadas

def solicita_chute():
    chute = input("\nChute uma letra que possa fazer parte da palavra secreta: ")
    chute = chute.strip().lower()
    return chute

def adiciona_letra_acertada(palavra_secreta, chute, letras_acertadas):
    print(f"\nVocê acertou o chute. A letra \"{chute}\" existe na palavra!")
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros, letras_acertadas):
    letras_faltando = conta_letras(letras_acertadas)
    print(f"\nEpa, você errou o chute. Ainda faltam {letras_faltando} letras para completar a palavra.")
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")


    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def verifica_se_perdeu(erros):
    enforcou = erros == 7
    return enforcou

def verifica_se_ganhou(letras_acertadas):
    acertou = "_" not in letras_acertadas
    return acertou

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, que pena! você foi enforcado!!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == '__main__':
    jogar()