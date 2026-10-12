'''Calculo de ano bisexto'''
def leap_year(year):
    '''Estrutura de decisão para avaliar se o ano é bisexto'''
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    if year % 4 == 0:
        return True
    return False
    
