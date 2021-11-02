def interface():
    print("*****************************")
    print("*   Jogo da adivinhação     *")
    print("*****************************")
    
def total_de_tentativas(total_de_tentativas,rodada,chute):
    numero_secreto = 42
    total_de_tentativas = 3
    rodada = 1

    while(total_de_tentativas > 0):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite o seu numero: "))
        print("você digitou: ", chute)


        if (chute == numero_secreto):
            print("Você acertou...")
            break
        elif(chute > numero_secreto):
            print("Seu chute foi maior que o número secreto.")
        elif(chute < numero_secreto):
            print("Seu chute foi menor que o numero secreto")
        else:
            print("Você errou..")
    
        
        rodada = rodada + 1
        total_de_tentativas = total_de_tentativas - 1

        print("Tentativas esgotadas")

interface()
total_de_tentativas('total_de_tentativas','rodada','chute')

