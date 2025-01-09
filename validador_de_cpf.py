"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- Priemeiro dígito
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys

cpf_enviado_pelo_usuario = input('CPF: ')
print('\nCPF recebido:', cpf_enviado_pelo_usuario, '\n')

entrada_cpf = re.sub(r'[^0-9]', '', cpf_enviado_pelo_usuario)

entrada_sequncial = entrada_cpf == entrada_cpf[0] * len(entrada_cpf)
if entrada_sequncial:
    print(f'{cpf_enviado_pelo_usuario} é inválido!\n')
    sys.exit()

nove_primeiros_digitos = entrada_cpf[:9]
dez_primeiros_digitos = entrada_cpf[:10]

soma_dos_numeros = 0
valores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
for i, digito in enumerate(nove_primeiros_digitos):
    soma_dos_numeros += int(digito) * valores[i]

multiplica_por_dez = 10
soma_dos_numeros *= multiplica_por_dez
resto_por_onze = soma_dos_numeros % 11
primeiro_digito = resto_por_onze if resto_por_onze <= 9 else 0
primeiro_digito_verificador = str(primeiro_digito)
print(f'O primeiro dígito do CPF é: {primeiro_digito_verificador}\n')

soma_dos_numeros = 0
valores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
for i, digito in enumerate(dez_primeiros_digitos):
    soma_dos_numeros += int(digito) * valores[i]

soma_dos_numeros *= multiplica_por_dez
resto_por_onze = soma_dos_numeros % 11

segundo_digito = resto_por_onze if resto_por_onze <= 9 else 0
segundo_digito_verificador = str(segundo_digito)
print(f'O segundo dígito do CPF é: {segundo_digito_verificador}\n')

cpf_gerado_pelo_calculo = nove_primeiros_digitos + primeiro_digito_verificador + segundo_digito_verificador

if entrada_cpf == cpf_gerado_pelo_calculo:
    print(f'O CPF {cpf_enviado_pelo_usuario} é validado!\n')
else:
    print(f'O CPF {cpf_enviado_pelo_usuario} é inválido!\n')