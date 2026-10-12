def steps(number):
    #Vejo se o número é inteiro positivo e diferente de 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    contador = 0
    while number > 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (number * 3) + 1
        contador += 1
    return contador

print(steps(1))