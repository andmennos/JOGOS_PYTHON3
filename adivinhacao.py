import random

def jogar():
    imprime_mensagem_inicial()
    numero_secreto = gera_numero_secreto()
    total_de_tentativas = define_dificuldade()
    print(f"\nVocê possui {total_de_tentativas} tentativas.")

    acertou = False
    perdeu = False
    tentativas = 0
    total_pontuacao = 1000
    ponto_final = 2

    while not acertou and not perdeu:

        chute = solicita_chute()

        if chute == numero_secreto:
            pontuacao = abs(calcula_pontuacao(tentativas, total_pontuacao, total_de_tentativas)) * ponto_final
            mensagem_vencedor(pontuacao)
            acertou = True

        elif chute > numero_secreto:
            print("\nVocê errou! O número que você chutou é maior que o número secreto.")
            tentativas += 1
            tentativas_restantes = conta_tentativas(total_de_tentativas, tentativas)

            if tentativas_restantes == 0:
                pontuacao = calcula_pontuacao(tentativas, total_pontuacao, total_de_tentativas) / ponto_final
                mensagem_perdedor(numero_secreto, pontuacao)
                perdeu = True
            else:
                if tentativas_restantes == 1:
                    print(f"Cuidado! Essa é sua última tentativa")
                else:
                    print(f"Você possui {tentativas_restantes} tentativas")

        elif chute < numero_secreto:
            print("\nVocê errou! O número que você chutou é menor que o número secreto.")
            tentativas += 1
            tentativas_restantes = conta_tentativas(total_de_tentativas, tentativas)

            if tentativas_restantes == 0:
                pontuacao = calcula_pontuacao(tentativas, total_pontuacao, total_de_tentativas) / ponto_final
                mensagem_perdedor(numero_secreto, pontuacao)
                perdeu = True
            else:
                print("\nTente de novamente\n")
                if tentativas_restantes == 1:
                    print(f"Cuidado! Essa é sua última tentativa")
                else:
                    print(f"Você possui {tentativas_restantes} tentativas")

def imprime_mensagem_inicial():
    print("**********************************")
    print("*Bem vindo ao Jogo da Adivinhação*")
    print("**********************************")

def gera_numero_secreto():
    numero_secreto = random.randrange(1, 101)
    return numero_secreto

def define_dificuldade(i=0):
    print("Nível de dificuldade:")
    print("Nível Fácil (1) - Médio (2) - Difícil (3)")

    while i < 1:
        total_de_tentativas = 0
        nivel = int(input("Digite o número respectivo do nível escolhido: "))

        if nivel == 1:
            total_de_tentativas = 20
            i += 1
        elif nivel == 2:
            total_de_tentativas = 10
            i += 1
        elif nivel == 3:
            total_de_tentativas = 5
            i += 1
        else:
            print("\nVocê deve definir um nível entre 1 e 3!\n")
    return total_de_tentativas

def conta_tentativas(total_de_tentativas, tentativas):
    tentativas_restantes = total_de_tentativas - tentativas
    return tentativas_restantes

def solicita_chute():
    chute = int(input("Chute um número entre 1 e 100: "))
    while chute < 1 or chute > 100:
        chute = int(input("Chute um número entre 1 e 100: "))
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
    print(f"Você digitou: {chute}.")
    return chute

def calcula_pontuacao(tentativas, total_pontuacao, total_de_tentativas):
    pontos_perdidos = tentativas + total_de_tentativas
    pontuacao = abs(total_pontuacao / pontos_perdidos)
    return pontuacao

def mensagem_vencedor(pontuacao):
    print(f"\nINCRÍVEL!! Você acertou e fez {pontuacao:.0f} pontos!")
    print("\nParabéns, você ganhou!!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'     \n")

def mensagem_perdedor(numero_secreto, pontuacao):
    print(f"\nQue pena, você perdeu! O número secreto era {numero_secreto}. Você fez {pontuacao:.0f} pontos!\n")
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
    print("       \_______/         \n")

if __name__ == "__main__":
    jogar()