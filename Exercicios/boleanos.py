temp = 750
n_neu = 600

def is_criticality_balanced(temp, n_neu):
    if temp < 800 and n_neu > 500 and temp * n_neu < 500000:
        return True
    else:
        False