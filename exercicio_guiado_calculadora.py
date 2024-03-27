while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Que tipo de operação deseja fazer? (+-/*)')

    numeros_validos = None

    try:
        num_1_int = int(numero_1)
        num_2_int = int(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Você não digitou números válidos:')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(f'resultado de {num_1_int} + {num_2_int} é: {num_1_int + num_2_int}')

    elif operador == '-':
        print(f'resultado de {num_1_int} - {num_2_int} é: {num_1_int - num_2_int}')

    elif operador == '/':
        print(f'resultado de {num_1_int} / {num_2_int} é: {num_1_int / num_2_int}')

    elif operador == '*':
        print(f'resultado de {num_1_int} x {num_2_int} é: {num_1_int * num_2_int}')

    

    sair = input('Quer sair? [s]im:').lower().startswith('s')
    
    if sair is True:
        print('você saiu')
        break