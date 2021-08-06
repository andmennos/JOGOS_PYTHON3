import adivinhacao
import forca


print("**********************************")
print("*****Escolha o que quer jogar*****")
print("***Forca (1) - Adivinhação (2)***")
print("**********************************")



jogo = int(input("Digite o número correspondente ao jogo escolhido: "))

if jogo == 1:
    print("\nJogando Forca")
    forca.jogar()

elif jogo == 2:
    print("\nJogando Adivinhação")
    adivinhacao.jogar()

print("\nFim do jogo")