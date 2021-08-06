import adivinhacao
import forca

def jogar():
    sair = False
    while not sair:
        print("********************************************")
        print("**********Escolha o que quer jogar**********")
        print("***Forca (1) - Adivinhação (2) - Sair(0)***")
        print("*********************************************")



        jogo = int(input("Digite o número correspondente ao jogo escolhido: "))

        if jogo == 1:
            print("**********************************")
            print("\n*********Jogando Forca**********\n")
            forca.jogar()

        elif jogo == 2:
            print("\n******Jogando Adivinhação*******\n")
            adivinhacao.jogar()

        elif jogo == 0:
            sair = True

if __name__ == '__main__':
        jogar()