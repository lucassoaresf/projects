def play():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    secret_word = "morango"

    wrong = False
    right = False

    while not right and not wrong:

        attempt = input("Escolha uma letra: ")

        index = 0
        for letter in secret_word:
            if attempt == letter:
                print(f"Encontrei a letra {letter} na posição {index}.")
            index = index + 1
        print("Jogando...")

    print("Fim de jogo!!!")

if __name__ == "__main__":
    jogar()
