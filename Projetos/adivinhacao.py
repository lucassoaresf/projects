import random


def play():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 31)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Selecione o nível: "))

    if nivel == 1:
        tentativas = 15
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}!!!")

        chute = int(input("Digite um número entre 1 e 30: "))
        print(f"Você digitou o número {chute}")

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 30.")
            continue

        if numero_secreto == chute:
            print(f"Você acertou e acabou com {pontos} pontos!!!")
            break
        elif chute > numero_secreto:
            print("Você errou, seu número foi maior que o número secreto.")
        elif chute < numero_secreto:
            print("Você errou, seu número foi menor que o número secreto.")
        lost = abs(numero_secreto - chute)
        pontos = pontos - lost

    print("Fim de jogo!!!")


if __name__ == "__main__":
    jogar()
