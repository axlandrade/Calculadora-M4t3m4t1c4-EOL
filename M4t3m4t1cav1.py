#Solicitando ao usuário que selecione a opção da calculadora.

opcao = int(input("Selecione a sua opção\n 1. Soma\n 2. Divisão\n"))

if opcao == 1: #Bloco de comandos que sera executado se a opção 1 for selecionada.
    soma = eval(input("Digite na forma 'a + b + ... + n' os valores que você quer somar.\n"))
    print(soma)
else:
    pass

if opcao == 2:
        divisao = eval(input("Digite na forma 'a/b' os numeros que voce quer dividir.\n"))
        print(divisao)
else:
    pass
