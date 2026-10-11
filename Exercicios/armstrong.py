'''number = 9
def is_armstrong_number(n0umber):

    digits = str(number)

    qtd_dig = len(digits)
    print(qtd_dig,digits)


    total = 0

    for digit in digits:
        total += int(digit) ** qtd_dig
        print(total)
    print(total)
    if total == number:
        return print(True)
    return print(False)


is_armstrong_number(number)'''

def is_armstrong_number(number):

    '''Valida se é menor que zero e se é igual a 0'''
    if number < 0:
      return print(False)
    if number == 0:
      return print(True)
    '''Criação de variaveis de apoio, num para não perder o 
    valor total e qtd_dig para descobri a quantidade de números'''
    num = number
    qtd_dig = 0
    '''Estrutura de repetição para descobri quantos dígitos tem o
    num.
    É uma forma diferente e mais díficil de se fazer por conta que eu preciso
    valida se o número é menor que 0, depois façõ a acrescentação de 1 e
    divido o número por 10 já o arredondando com //'''
    while num > 0:
       qtd_dig += 1
       num //= 10
       print ('Quantidade de Dígitos',qtd_dig)
       print ('atualização dos números',num)
    '''Criação de variveis como o num para manter o valor intacto e
    total para somatório para verificar se o número é igual ao number'''
    num = number
    total = 0

    while num > 0:
       digit = num % 10
       total += digit ** qtd_dig
       num //= 10 
       print('Verificar o ultimo digito',digit)
       print('Verificar as sómatorias',total)
       print('Divisão de resto',num)

    return total == number
       
       
is_armstrong_number(153)