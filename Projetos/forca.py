def play():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    secret_word = "morango".upper()
    word_true = ["_", "_", "_", "_", "_", "_", "_"]

    wrong = False
    right = False
    error = 0

    print(word_true)

    while not right and not wrong:

        attempt = input("Escolha uma letra: ")
        attempt = attempt.strip().upper()

        if attempt in secret_word:
            index = 0
            for letter in secret_word:
                if attempt == letter:
                    word_true[index] = letter
                index += 1
        else:
            error += 1
            print(f"Você errou! faltam {7-error} tentativas.")

        if error == 7:
            break
        if "_" not in word_true:
            break
        print(word_true)

    if(right):
        print("Parabéns você acertou a palavra secreta!!!")
    else:
        print("Não foi dessa vez que você conseguiu :(")
    print("Fim de jogo!!!")

if __name__ == "__main__":
    play()
