"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calcula o tempo restante que a lasanha ainda precisa ficar no forno."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calcula o tempo de preparo com base no número de camadas."""
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcula o tempo total usado na cozinha (preparo + forno). """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time