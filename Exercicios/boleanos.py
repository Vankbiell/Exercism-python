'''-----Primeira parte---------------------------------------------------------------------------------------'''

temp = 750
n_neu = 600

def is_criticality_balanced(temp, n_neu):
    if temp < 800 and n_neu > 500 and temp * n_neu < 500000:
        return print(True)
    else:
        return print(False)

is_criticality_balanced(temp, n_neu)
'''-----Segunda parte---------------------------------------------------------------------------------------'''

vol = 200
cor = 50
the = 15000

def reactor_efficiency(vol, cor, the):
    generated_power = vol * cor
    percent = (generated_power / the) * 100

    '''Otimização do código'''
    if percent >= 80:
        return print('green')
    elif percent >= 60:
        return print('orange')
    elif percent >= 30:
        return print('red')
    else:
        return print('black')
    
''' if percent >= 80:
        return print('green')
    elif percent < 80 and percent >= 60:
        return print('orange')
    elif percent < 60 and percent >= 30:
        return print('red')
    else:
        return print('black')'''

reactor_efficiency(vol, cor, the)

'''-----Terceira parte---------------------------------------------------------------------------------------'''
temp = 1000
n_p = 30
thr = 5000
def fail_safe(temp, n_p, thr):
    tt = temp * n_p
    if tt < thr * 0.9:
        return print('LOW')
    elif tt < thr * 0.1 and tt > 0:
        return print('NORMAL')
    else:
        return print('DANGER')

fail_safe(temp, n_p, thr)