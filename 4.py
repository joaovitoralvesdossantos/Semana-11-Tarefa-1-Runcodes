# Inverte um número inteiro
def invertido(numero):
    return int(str(numero)[::-1])

# Função principal
def main():

    #entrada de dados
    numero_invertido = int(input("Digite um número inteiro: "))
    
    #processamento
    numero_invertido = invertido(numero_invertido)
    
    #saida de dados
    print(f"O número invertido é: {numero_invertido}")

# Chama a função principal
if __name__ == '__main__':
    main()