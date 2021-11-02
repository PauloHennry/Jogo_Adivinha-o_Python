
def interface():
    print("*****************************")
    print("*   Jogo da adivinhação     *")
    print("*****************************")
    

def numero_secreto(chute):
    while True:
        numero_secreto = 42
        chute = int(input("Digite um numero: "))
        print("Você digitou: ",chute)

        if (chute == numero_secreto):
            print("Você acertou...")
        elif(chute > numero_secreto):
            print("Seu chute foi maior que o número secreto.")
        elif(chute < numero_secreto):
            print("Seu chute foi menor que o numero secreto")
        else:
            print("Você errou..")

interface()
numero_secreto('chute')




