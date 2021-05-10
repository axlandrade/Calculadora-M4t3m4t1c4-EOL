import Calculadora_M4t3m4t1ca

def area_do_quadrado():
    lado = int(input("Insira o lado do seu quadrado\n"))
    area_quadrado = int(lado**2)
    print("A área do seu quadrado vale:", area_quadrado)

def area_do_retangulo():
    base = int(input("Insira o valor da base do retângulo\n"))
    altura = int(input("Insira o valor da altura do retângulo\n"))
    area_retangulo = base * altura
    if base == altura:
        print("Esse retângulo é um quadrado.")
        print("A área do seu quadrado vale:", area_retangulo)
    else:
        print("A área do seu retângulo vale:", area_retangulo)
    

def area_do_triangulo():
    opcao_tri = int(input("Seu triângulo é retângulo?\n 1. Sim\n 2. Não\n 3. Sair"))
    if opcao_tri == 3:
        retornar_menu()
    else:
        pass
        
    if opcao_tri == 1:
        cateto_a = int(input("Insira o valor de um cateto\n"))
        cateto_b = int(input("Insira o valor de outro cateto\n"))
        area_triangulo = cateto_a*cateto_b
        print("A área do seu triângulo vale:", area_triangulo)
    else:
        pass

def menu_areas():
    opcao_a = int(input("Selecione a sua opção:\n 1. Quadrado\n 2. Retângulo\n"))
    if opcao_a == 1:
        area_do_quadrado()
        Calculadora_M4t3m4t1ca.retornar_menu()
    else:
        pass

    if opcao_a == 2:
        area_do_retangulo()
        Calculadora_M4t3m4t1ca.retornar_menu()
    else:
        pass
