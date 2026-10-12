'''Calculo de ano bisexto'''
def leap_year(year):
    '''Estrutura de decisão para avaliar se o ano é bisexto'''
    if year % 100 == 0:
        # Para saber da exceção, se ele for divisivél por 100 e por 400 é True se não False
        if year % 400 == 0:
            return True
        return False
        # Números divisivéis por 4
    if year % 4 == 0:
        return True
    return False
    
