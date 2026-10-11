"""Módulo para calcular a quantidade de grãos em um tabuleiro de xadrez."""
def square(number):
    """Calcula a quantidade de grãos em uma casa específica."""
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

def total():
    """Calcula o total de grãos em todo o tabuleiro de xadrez."""
    return (2 ** 64) - 1
