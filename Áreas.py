def area_do_quadrado():
    lado = int(input("Insira o lado do seu quadrado\n"))
    area_quadrado = int(lado**2)
    print("A área do seu quadrado vale:", area_quadrado)

def area_do_retangulo():
    base = int(input("Insira o valor da base do retângulo\n"))
    altura = int(input("Insira o valor da altura do retângulo\n"))
    area_retangulo = base * altura
    print("A área do seu retângulo vale:", area_retangulo)
