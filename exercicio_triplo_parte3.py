"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('me fala ai seu nome por favor, preu tira uma moto nele: ')
checador_tamanho = len(nome)

try:
    if checador_tamanho <= 4:
        print ('seu nome é curto')
    elif checador_tamanho >= 5 and checador_tamanho <= 6:
        print ('bonde do nome médio')
    elif checador_tamanho > 6:
        print ('tu é nómudo em q isso')
except:
    print('para de escrever baboseira faz favora')