# Faz a adição do percentual de juros no valor inicial
def precofinal(valor, juros):
    totalantigo = valor
    total = totalantigo * (1 + juros / 100)
    dobro = valor * 2
    vezes = 1

# Loop que é quebrado apenas quando chega no valor dobrado do valor inicial
    while total <= dobro:
        totalantigo = total
        total = totalantigo * (1 + juros / 100)
        vezes += 1
    return vezes


# Função principal
def main():

    #entrada de dados
    valor = float(input("Digite o valor: "))
    juros = float(input("Digite o percentual de juros ao ano: "))

    #processamento
    resultado = precofinal(valor, juros)

    #saida de dados
    print(f"Serão necessarios {resultado} anos para que o valor inicial seja dobrado.")

# Chama a função principal
if __name__ == '__main__':
    main()