import random

class jokenpo:
    elementos = ["pedra", "papel", "tesoura"]
    
    @staticmethod
    def jogada_da_maquina():
        escolha = random.choice(jokenpo.elementos)
        print(f"O oponente jogou: {escolha}")
        return escolha  
while True:         
    print("Bem vindo ao jogo de Jokenpo virtual!")
    jogada=input("digite sua jogada: [pedra] - [papel] ou [tesoura]! ou tecle [0] para encerrar!")
    
    maquina=jokenpo.jogada_da_maquina()
    
    if jogada == 0: 
        break
    elif jogada == maquina:
        print("empate!")    
    elif (jogada == "pedra" and maquina == "tesoura") or \
          (jogada == "papel" and maquina == "pedra") or \
          (jogada == "tesoura" and maquina == "papel"):
        print("voce venceu!")
    else:
        print("A maquina venceu!")
    continue
    