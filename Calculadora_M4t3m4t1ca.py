import PySimpleGUI as sg
from sympy import *
   
sg.ChangeLookAndFeel('DarkBlue')

layout = [
    [sg.Text('Expressão: '), sg.Input(key='expressao', size=(45,1))],
    [sg.HorizontalSeparator(color='black')],
    [sg.Button('Expressão Simples', key='simples'), sg.Button('Equação', key='equacao'), sg.Button('Inequação', key='inequacao'), sg.Button('Limite', key='limite'), sg.Button('Derivada', key='derivada'), sg.Button('Integral Ind.', key='integral_ind')],
    [sg.Output(size=(54,20), key='output')],
    [sg.Text('Programa desenvolvido por Axl Andrade (UFRRJ-UNESA)')]
]

window = sg.Window('M4t3m4t1ca',layout , resizable=True)

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
        
        sg.theme('Topanga')
    
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
    
window.close()
