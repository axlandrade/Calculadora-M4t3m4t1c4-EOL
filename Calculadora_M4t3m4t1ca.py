import PySimpleGUI as sg
from sympy import *
   
sg.ChangeLookAndFeel('DarkBlue')

left_column = [
    [sg.Text('Expressão: '), sg.InputText("", key='expressao', size=(45,1))],
    [sg.HorizontalSeparator(color='black')],
    [sg.Button('Expressão Simples', key='simples'), sg.Button('Equação', key='equacao'), sg.Button('Inequação', key='inequacao'), sg.Button('Limite', key='limite'), 
    sg.Button('Derivada', key='derivada'), sg.Button('Integral Ind.', key='integral_ind')],
    [sg.Output(size=(54,20), key='output')],
    [sg.HorizontalSeparator()],
    [sg.Button('7', key = '7'), sg.Button('8', key = '8'), sg.Button('9', key = '9'), sg.Button('-', key = '-'), sg.Button('/', key = '/')],
    [sg.Button('4', key = '4'), sg.Button('5', key = '5'), sg.Button('6', key = '6'), sg.Button('+', key = '+'), sg.Button('*', key = '*'),],
    [sg.Button('1', key = '1'), sg.Button('2', key = '2'), sg.Button('3', key = '3'), sg.Button('.', key = '.'), sg.Button('^', key = '^'),],
    [sg.Button('0', key = '0'), sg.Button('Limpar', key = 'limpar')],
    [sg.Text("Símbolos: "), sg.Button('X', key = 'X'), sg.Button('√', key = 'raiz'), sg.Button('(', key = '('), sg.Button (')', key = ')')],
    [sg.Text('Programa desenvolvido por Axl Andrade (UFRRJ-UNESA)')]
]

right_column = [
    [sg.Button('Área do quadrado', key = 'quadrado')],
    [sg.Button('Área do triângulo', key = 'triangulo')],
    [sg.Button('Área do retângulo', key = 'retangulo')]
]

layout = [[sg.Column(left_column, element_justification='c'), sg.VSeparator(), sg.Column(right_column, element_justification='c')]]

window = sg.Window('M4t3m4t1c4', layout, element_padding=(2,2), resizable=True)

while True:
    event, values = window.read()
    
    if event == '7':
        expressao = values['expressao']
        expressao = values['expressao'] + str(7)
        window.FindElement('expressao').Update(expressao)
        
    if event == '8':
        expressao = values['expressao']
        expressao = values['expressao'] + str(8)
        window.FindElement('expressao').Update(expressao)
        
    if event == '9':
        expressao = values['expressao']
        expressao = values['expressao'] + str(9)
        window.FindElement('expressao').Update(expressao)
        
    if event == '4':
        expressao = values['expressao']
        expressao = values['expressao'] + str(4)
        window.FindElement('expressao').Update(expressao)
        
    if event == '5':
        expressao = values['expressao']
        expressao = values['expressao'] + str(5)
        window.FindElement('expressao').Update(expressao)
        
    if event == '6':
        expressao = values['expressao']
        expressao = values['expressao'] + str(6)
        window.FindElement('expressao').Update(expressao)
        
    if event == '1':
        expressao = values['expressao']
        expressao = values['expressao'] + str(1)
        window.FindElement('expressao').Update(expressao)
        
    if event == '2':
        expressao = values['expressao']
        expressao = values['expressao'] + str(2)
        window.FindElement('expressao').Update(expressao)
        
    if event == '3':
        expressao = values['expressao']
        expressao = values['expressao'] + str(3)
        window.FindElement('expressao').Update(expressao)
        
    if event == '0':
        expressao = values['expressao']
        expressao = values['expressao'] + str("0")
        window.FindElement('expressao').Update(expressao)
        
    if event == '-':
        expressao = values['expressao']
        expressao = values['expressao'] + str("-")
        window.FindElement('expressao').Update(expressao)
        
    if event == '+':
        expressao = values['expressao']
        expressao = values['expressao'] + str("+")
        window.FindElement('expressao').Update(expressao)
        
    if event == '.':
        expressao = values['expressao']
        expressao = values['expressao'] + str(".")
        window.FindElement('expressao').Update(expressao)
        
    if event == '/':
        expressao = values['expressao']
        expressao = values['expressao'] + str("/")
        window.FindElement('expressao').Update(expressao)
        
    if event == '*':
        expressao = values['expressao']
        expressao = values['expressao'] + str("*")
        window.FindElement('expressao').Update(expressao)
        
    if event == '^':
        expressao = values['expressao']
        expressao = values['expressao'] + str("**")
        window.FindElement('expressao').Update(expressao)
        
    if event == 'X':
        expressao = values['expressao']
        expressao = values['expressao'] + str("x")
        window.FindElement('expressao').Update(expressao)
        
    if event == 'raiz':
        expressao = values['expressao']
        
        layout = [[sg.Text("Digite o número que você deseja na raiz"), sg.InputText(key = 'x_raiz')],
                  [sg.Submit('Confirmar'), sg.Submit('Cancelar')]
                  ]
        
        popup_xraiz = sg.Window('Número da raiz', layout)
        
        event, values = popup_xraiz.read()
        
        x_raiz = values['x_raiz']
        popup_xraiz.close()
        
        expressao = expressao + str("sqrt(") + str(x_raiz) + str(")")
        window.FindElement('expressao').Update(expressao)
        
    if event == '(':
        expressao = values['expressao']
        expressao = values['expressao'] + str("(")
        window.FindElement('expressao').Update(expressao)
        
    if event == ')':
        expressao = values['expressao']
        expressao = values['expressao'] + str(")")
        window.FindElement('expressao').Update(expressao)
        
    if event == 'limpar':
        expressao = values['expressao']
        expressao = ""
        window.FindElement('expressao').Update(expressao)
    
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
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]]

        popupq = sg.Window('Área do quadrado', layout)
        while True:
            event, values = popupq.read()

            if event == 'Cancelar' or event == None:
                break
            
            if event == 'Confirmar':
                lado_q = values['lado']
                area = int(lado_q)**2
                init_printing()
                print("Sua área vale:\n", area)
                print("\n")
                break
            
        popupq.close()

    if event == 'triangulo':

        layout = [[sg.Text('Insira aqui a base e a altura do seu triângulo')],
                  [sg.Text('Base:'), sg.InputText(key = 'base')],
                  [sg.Text('Altura'), sg.InputText(key = 'altura')],
                  [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]]

        popupt = sg.Window('Área do triângulo', layout)
        while True:
            event, values = popupt.read()
            
            if event == 'Cancelar' or event == None:
                break
            
            if event == 'Confirmar':
                base_t = values['base']
                alt_t = values['altura']
                area = (int(base_t) * int(alt_t))/2
                init_printing()
                print("Sua área vale:\n", area)
                print("\n")
                break
            
        popupt.close()

    
    if event == 'retangulo':
        
        layout = [[sg.Text('Insira aqui a base e a altura do seu retângulo')],
                  [sg.Text('Base:'), sg.InputText(key = 'base')],
                  [sg.Text('Altura'), sg.InputText(key = 'altura')],
                  [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]]
        
        popupr = sg.Window('Área do retângulo', layout)
        while True:
            event, values = popupr.read()
            
            if event == 'Cancelar' or event == None:
                break
            
            if event == 'Confirmar':
                base_r = values['base']
                alt_r = values['altura']
                area = (int(base_r) * int(alt_r))
                init_printing()
                print("Sua área vale:\n", area)
                print("\n")
                break  
        
        popupr.close()   
    
window.close()
