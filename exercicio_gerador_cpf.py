import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))

# # verificação do primeiro digito no bloco seguinte
nove_digitos = cpf[:9]
primeiro_multiplicador_regressivo = 10
primeiro_digito = 0
primeiro_resultado = 0

for primeiro_digito in nove_digitos:
    primeiro_resultado += int(primeiro_digito) * primeiro_multiplicador_regressivo
    primeiro_multiplicador_regressivo -= 1
primeiro_digito = ((primeiro_resultado * 10) % 11)
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
# print(primeiro_digito)

# verificação do segundo digito no bloco seguinte
dez_digitos = nove_digitos + str(primeiro_digito)
segundo_multiplicador_regressivo = 11
segundo_digito = 0
segundo_resultado = 0

for segundo_digito in dez_digitos:
    segundo_resultado += int(segundo_digito) * segundo_multiplicador_regressivo
    segundo_multiplicador_regressivo -= 1
segundo_digito = ((segundo_resultado * 10) % 11)
segundo_digito = segundo_digito if segundo_digito <= 9 else 0
# print(segundo_digito)

novo_cpf = f'{cpf}{primeiro_digito}{segundo_digito}'
print(novo_cpf)