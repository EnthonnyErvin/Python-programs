import random

nove_primeiros_digitos = ''

for i in range(9):
    nove_primeiros_digitos += str(random.randint(0, 9))

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

dez_primeiros_digitos = nove_primeiros_digitos + primeiro_digito_verificador

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

print('Novo CPF gerado:', cpf_gerado_pelo_calculo, '\n')