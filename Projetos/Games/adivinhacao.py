import random


def play():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1, 31)
    chance = 0
    points = 1000

    print("Qual nível de dificuldade?")
    print("(1) - Fácil\n"
          "(2) - Médio\n"
          "(3) - Difícil")

    level = int(input("Selecione o nível: "))

    if level == 1:
        chance = 15
    elif level == 2:
        chance = 10
    else:
        chance = 5

    for round in range(1, chance + 1):
        print(f"Tentativa {round} de {chance}!!!")

        attempt = int(input("Digite um número entre 1 e 30: "))
        print(f"Você digitou o número {attempt}")

        if attempt < 1 or attempt > 30:
            print("Você deve digitar um número entre 1 e 30.")
            continue

        if secret_number == attempt:
            print(f"Você acertou e acabou com {points} pontos!!!")
            break
        elif attempt > secret_number:
            print("Você errou, seu número foi maior que o número secreto.")
        elif attempt < secret_number:
            print("Você errou, seu número foi menor que o número secreto.")
        lost = abs(secret_number - attempt)
        points = points - lost

    print("Fim de jogo!!!")


if __name__ == "__main__":
    play()
