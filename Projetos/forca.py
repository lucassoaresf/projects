import random

def play():

    opening_message()
    secret_word = loading_word()

    word_true = ["_" for letter in secret_word] #Acrescenta um _ a cada letra da palavra secreta.
    print(word_true)

    wrong = False
    right = False
    error = 0



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

        wrong = error == 7
        right = "_" not in word_true
        print(word_true)

    if(right):
        print("Parabéns você acertou a palavra secreta!!!")
    else:
        print(f"Não foi dessa vez que você conseguiu, a palavra secreta era {secret_word}")
    print("Fim de jogo!!!")


def opening_message():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def loading_word(): #É utilizado um aquivo txt, com leituras por linha como palavras secretas.
    archive = open("palavras.txt", "r", encoding="utf-8")
    word = []

    for line in archive:
        line = line.strip()
        word.append(line)

    archive.close()

    number = random.randrange(0, len(word))
    secret_word = word[number].upper()
    return secret_word


if __name__ == "__main__":
    play()