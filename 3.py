# Verifica qual número é maior e menor
def conjuto():
    contador = 0

    print("Digite um número, utilize '0' para finalizar.")
    numero = int(input(""))
    maior = numero
    menor = numero

    # Loop para verificação
    while True:
        resposta = int(input())
        if resposta == 0:
            break
        if resposta > maior:
            maior = resposta
        if resposta < menor:
            menor = resposta
            
    # Chamada
    if numero > 0:
        print(f"O maior número da lista foi: {maior}")
        print(f"O menor número da lista foi: {menor}")

# Função principal
def main():
    # Chama a função que faz os cálculos
    conjuto()

# Executa o programa
if __name__ == "__main__":
    main()
