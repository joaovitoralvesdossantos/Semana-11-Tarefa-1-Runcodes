# Base
def data(salario, divida):
    mes = 10
    ano = 2016

    # loop até que a dívida seja maior que o salário
    while divida <= salario:
        divida *= 1.15
    # aumenta o salário em 5% apenas em março
        if mes == 3:
            salario *= 1.05
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1
    print(f"{mes}/{ano}")

# Função principal
def main():

    #entrada de dados
    salario = float(input("Digite o valor do salário: "))
    divida = float(input("Digite o valor do dívida: "))
    
    #saida de dados
    data(salario, divida) 

# Chama a função principal
if __name__ == '__main__':
    main()