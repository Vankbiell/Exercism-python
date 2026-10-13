'''Funções para saber qual tipo do Triângulo'''
def equilateral(sides):
    '''Saber se existe algum número menor ou igual a zero'''
    for side in sides:
        if side <= 0:
            return False

    #Otimização do código feito abaixo utilizando all()
    once_side = sides[0]
    return all(side == once_side for side in sides )


    #Estrutura de Repetição para percorrer o vetor e saber se existe numeros diferentes ao primeiro armazenado
    #once = sides[0]
    #for side in sides:
        #if side != once:
            #return False
    #return True

def isosceles(sides):
    '''Saber se existe algum número menor ou igual a zero'''
    for side in sides:
        if side <= 0:
            return False
    # Armazenamento de cada varivél dentro de cada indice do vetor
    once_side = sides[0]
    second_side = sides[1]
    third_side = sides[2]
    # Testes para saber se os números são iguais e se a soma entre os números iguais são maiores ou iguais ao outro lado que não foi somado
    if once_side == second_side and (once_side + second_side) >= third_side:
        return True
    if once_side == third_side and (once_side + third_side) >= second_side:
        return True
    if second_side == third_side and (second_side + third_side) >= once_side:
        return True
    return False


def scalene(sides):
    '''Saber se existe algum número menor ou igual a zero'''
    for side in sides:
        if side <= 0:
            return False
    # Otimização de armazenamento de cada varivél dentro de cada indice do vetor
    once_side, second_side, third_side = sides

    if (once_side + second_side) <= third_side or (once_side + third_side) <= second_side or (second_side + third_side) <= once_side:
        return False
    if once_side != second_side and once_side != third_side and second_side != third_side:
        return True
    return False
        
