import random

class Jokenpo:
    elementos = ["pedra", "papel", "tesoura"]
    
    @staticmethod
    def jogada_da_maquina():
        
        escolha = random.choice(Jokenpo.elementos)
        return escolha

print("===== Bem-vindo ao Jokenpo Virtual! =====")

while True:
    jogada = input("\nSua jogada [pedra, papel, tesoura] ou [0] para sair: ").lower()

    if jogada == "0":
        print("Encerrando o jogo... Até a próxima!")
        break

    if jogada in Jokenpo.elementos:
        maquina = Jokenpo.jogada_da_maquina()
        
        print(f"\nVocê jogou: {jogada}")
        print(f"O oponente jogou: {maquina}")
        print("-" * 20)

        # Lógica para decidir o vencedor
        if jogada == maquina:
            print("🤝 EMPATE!")
        elif (jogada == "pedra" and maquina == "tesoura") or \
             (jogada == "papel" and maquina == "pedra") or \
             (jogada == "tesoura" and maquina == "papel"):
            print("🎉 VOCÊ VENCEU!")
        else:
            print("🤖 A MÁQUINA VENCEU!")
        print("-" * 20)
    else:
        print("❌ Opção inválida! Digite pedra, papel ou tesoura.")