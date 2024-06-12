"""
cpf = input('CPF: ')

cpf_enviado = cpf.replace('.', '').replace('-', '').replace(' ', '')

# Usando módulo re

import re, sys

cpf_enviado= re.sub(r'[^0-9]', '', cpf)    # Tudo que não for um número, substitua por nada...

entrada_sequencial = cpf == cpf[0] * len(cpf)

if entrada_sequencial:
    print('Dados sequenciais...')
    sys.exit()
"""

import random

for _ in range(100):
    # Primeiro Dígito

    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10

    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Segundo Dígito

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # Novo CPF

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado)

"""
if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido!')
else:
    print('CPF inválido!')
"""