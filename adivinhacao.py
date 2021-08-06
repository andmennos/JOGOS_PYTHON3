import random

def jogar():
    print("**********************************")
    print(" Bem vindo ao Jogo da Adivinhação")
    print("**********************************")

    print("Nível de dificuldade:")
    print("Nível (1) Fácil - (2) Médio - (3) Difícil")

    numero_secreto = random.randrange(1, 101)
    pontuacao = 1000
    perdeu = 800
    tentativas = 1
    total_de_tentativas = 0
    i = 0
    cont = 0

    while i < 1:

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

    for tentativas in range(1, total_de_tentativas + 1):
        print(f"Tentativa {tentativas} de {total_de_tentativas}.")
        chute = int(input("Chute um número entre 1 e 100: "))
        print(f"Você digitou: {chute}.")

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100! Perdeu uma tentativa")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"INCRÍVEL!! Você acertou e fez {pontuacao} pontos!")
            break

        elif maior:
            print("Você errou! O número que você chutou é maior que o número secreto.")
            pontos_perdidos = abs(chute - numero_secreto)
            pontuacao = pontuacao - pontos_perdidos
            if tentativas == total_de_tentativas:
                pontuacao = pontuacao - perdeu
                print(f"Que pena, você perdeu! O número secreto era {numero_secreto}. Você fez {pontuacao} pontos.")
            else:
                print("\nTente de novo\n")

        elif menor:
            print("Você errou! O número que você chutou é menor que o número secreto.")
            pontos_perdidos = abs(chute - numero_secreto)
            pontuacao = pontuacao - pontos_perdidos
            if tentativas == total_de_tentativas:
                pontuacao = pontuacao - perdeu
                print(f"Que pena, você perdeu! O número secreto era {numero_secreto}. Você fez {pontuacao} pontos.")
            else:
                print("\nTente de novo\n")

    print("\nFim do jogo")

if __name__ == "__main__":
    jogar()