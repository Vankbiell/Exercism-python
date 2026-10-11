"""Módulo para validação de números de Armstrong."""


def is_armstrong_number(number):
    """Verifica se um número inteiro é um número de Armstrong."""
    # Valida se é menor que zero e se é igual a 0
    if number < 0:
        return False
    if number == 0:
        return True

    # Criação de variáveis de apoio: num para não perder o
    # valor total e qtd_dig para descobrir a quantidade de dígitos
    num = number
    qtd_dig = 0

    # Estrutura de repetição para descobrir quantos dígitos tem o número
    while num > 0:
        qtd_dig += 1
        num //= 10

    # Reinicialização de num e acumulador total para calcular
    # a soma das potências de cada dígito
    num = number
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** qtd_dig
        num //= 10

    return total == number
       
