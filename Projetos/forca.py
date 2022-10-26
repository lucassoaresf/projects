def play():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    secret_word = "morango"
    word_true = ["_", "_", "_", "_", "_", "_", "_"]

    wrong = False
    right = False

    print(word_true)

    while not right and not wrong:

        attempt = input("Escolha uma letra: ")
        attempt = attempt.strip()

        index = 0
        for letter in secret_word:
            if attempt.upper() == letter.upper():
                word_true[index] = letter
            index = index + 1

        print(word_true)

    print("Fim de jogo!!!")

if __name__ == "__main__":
    play()
