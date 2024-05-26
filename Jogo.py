import random

opcao = ["pedra", "papel", "tesoura"]

escolha_jogador = input("Escolha entre papel, tesoura ou pedra: ")

escolha_computador = random.choice(opcao)

if escolha_jogador == escolha_computador:
    resultado = "Empate"
elif (escolha_jogador == "Pedra" and escolha_computador == "Tesoura") or \
     (escolha_jogador == "Papel" and escolha_computador == "Pedra") or \
     (escolha_jogador == "Tesoura" and escolha_computador == "Papel"):
     resultado = "Jogador venceu"
else:
     resultado = "Computador venceu"

print(f"O jogador escolher {escolha_jogador} ")
print(f"O computador escolheu {escolha_computador}")
print(f"O resultado é: {resultado}")