import forca
import adivinhacao

def choose_game():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    game = int(input("Qual jogo será escolhido: "))

    if game == 1:
        print("Jogo da Forca")
        forca.play()

    elif game == 2:
        print("Jogo da Adivinhação")
        adivinhacao.play()

if __name__ == "__main__":
    choose_game()
