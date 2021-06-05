import PySimpleGUI as sg
from sympy import *
   
sg.ChangeLookAndFeel('DarkBlue')

left_column = [
    [sg.Text('Expressão: '), sg.Input(key='expressao', size=(45,1))],
    [sg.HorizontalSeparator(color='black')],
    [sg.Button('Expressão Simples', key='simples'), sg.Button('Equação', key='equacao'), sg.Button('Inequação', key='inequacao'), sg.Button('Limite', key='limite'), 
    sg.Button('Derivada', key='derivada'), sg.Button('Integral Ind.', key='integral_ind')],
    [sg.Output(size=(54,20), key='output')],
    [sg.Text('Programa desenvolvido por Axl Andrade (UFRRJ-UNESA)')]
]

right_column = [
    [sg.Button('Área do quadrado', key = 'quadrado')],
    [sg.Button('Área do triângulo', key = 'triangulo')],
    [sg.Button('Área do retângulo', key = 'retangulo')]
]

layout = [[sg.Column(left_column, element_justification='c'), sg.VSeparator(), sg.Column(right_column, element_justification='c')]]

window = sg.Window('M4t3m4t1c4', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == 'simples':
        simples = values['expressao']
        sol = eval(simples)
        init_printing()
        print("Sua solução é:\n")
        pprint(sol)
        print("\n")
        
    if event == 'equacao':
        x = symbols('x')
        equacao = values['expressao']
        sol = solveset(equacao)
        init_printing()
        print("Sua solução é:\n")
        pprint(sol, wrap_line=False, use_unicode=True)
        print("\n")
        
    if event == 'inequacao':
        x = symbols('x')
        inequacao = values['expressao']
        sol = solveset(inequacao, x, domain=S.Reals)
        init_printing()
        print("Sua solução é:\n")
        pprint(sol)
        print("\n")
        
    if event == 'limite':
        expr = values['expressao']
        
        layout = [[sg.Text('Digite aqui o valor para qual x se aproxima')],
                  [sg.InputText(key='x_tende')],
                  [sg.Submit(), sg.Cancel()]]
    
        popupx = sg.Window('De qual valor x se aproxima', layout)
    
        event, values = popupx.read()
        x_apr = values['x_tende']
        popupx.close()
        
        x = symbols('x')
        
        limite_expr = limit(expr, x, x_apr)
        init_printing()
        print("Seu limite vale:\n")
        pprint(limite_expr)
        print("\n")
    
    if event == 'derivada':
        x = symbols('x')
        expr = values['expressao']
        derivada_expr = diff(expr)
        init_printing()
        print("Sua derivada retorna:\n")
        pprint(derivada_expr)
        print("\n")
    
    if event == 'integral_ind':
        x = symbols('x')
        expr = values['expressao']
        integral_expr = integrate(expr, x)
        init_printing()
        print("Sua integral retorna: ")
        pprint(integral_expr)
        print("\n")

    if event == 'quadrado':

        layout = [[sg.Text('Digite o valor do lado do seu quadrado')],
            [sg.InputText(key = 'lado')],
            [sg.Submit(), sg.Cancel()]]

        popupq = sg.Window('Área do quadrado', layout)

        event, values = popupq.read()

        lado_q = values['lado']
        popupq.close()

        area = int(lado_q)**2
        init_printing()
        print("Sua área vale:\n", area)
        print("\n")

    if event == 'triangulo':

        layout = [[sg.Text('Insira aqui a base e a altura do seu triângulo')],
        [sg.Text('Base:'), sg.InputText(key = 'base')],
        [sg.Text('Altura'), sg.InputText(key = 'altura')],
        [sg.Submit(), sg.Cancel()]]

        popupt = sg.Window('Área do triângulo', layout)

        event, values = popupt.read()
        base_t = values['base']
        alt_t = values['altura']
        popupt.close()

        area = (int(base_t) * int(alt_t))/2
        init_printing()
        print("Sua área vale:\n", area)
        print("\n")     
    
window.close()
