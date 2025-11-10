# Faz a soma dos numeros inteiros positivos
def conjuto():
    soma = 0
    contador = 0
    print("Digite um número, utilize '0' para finalizar.")
    
    while True:
        resposta = int(input())
        if resposta == 0:
            break
        soma += resposta
        contador += 1

    if contador > 0:
        media = soma / contador
        print(f"A média dos números da lista foi: {media:.2f}")

# Função principal
def main():
    # Chama a função que faz os cálculos
    conjuto()

# Executa o programa
if __name__ == "__main__":
    main()
