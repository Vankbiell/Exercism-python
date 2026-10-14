'''Respostas de Bob'''
def response(hey_bob):
    '''Primeiro se que responde Sure a qualquer pergunta.'''
    # No [-n] o menos corresponde aos ultimos caractéres, no códico eu verifico o ultimo caractere.
    fim_de_texto = hey_bob[-1] 

    # Verifica se a ultima letra é igual a ?.
    if fim_de_texto == '?' in hey_bob:
        return 'Sure.'

    # .isupper() é uma função do python que verifica se o texto todo está em caixa alta.
    if hey_bob.isupper():
        return 'Whoa, chill out!'

    # Combinação das duas estruturas de decisão acima com o and.
    if hey_bob.isupper() and (fim_de_texto == '?' in hey_bob):
        return "Calm down, I know what I'm doing!"

    # Se a variavél só tem espaços com o .isspace() ; Verifica se não 
    if hey_bob.isspace() or not hey_bob:
        return  'Fine. Be that way!'
    
    return 'Whatever'


print(response("WHAT'S GOING ON?"))