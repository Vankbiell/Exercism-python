    '''Respostas de Bob'''
    def response(hey_bob):
        # 1. Primeiro, removemos todos os espaços em branco do início e do fim.
        # Isso resolve o problema de frases que terminam com espaços.
        hey_bob = hey_bob.strip()
        
        # 2. Verifica se a string ficou vazia (silêncio).
        if not hey_bob:
            return 'Fine. Be that way!'
        
        # Criamos variáveis booleanas para deixar o código limpo e fácil de ler.
        eh_pergunta = hey_bob.endswith('?')
        esta_gritando = hey_bob.isupper()

        # 3. Se for uma pergunta gritada (Grito + Interrogação).
        if esta_gritando and eh_pergunta:
            return "Calm down, I know what I'm doing!"

        # 4. Se for apenas uma pergunta comum.
        elif eh_pergunta:
            return 'Sure.'

        # 5. Se estiver apenas gritando.
        elif esta_gritando:
            return 'Whoa, chill out!'
        
        # 6. Qualquer outra coisa.
        return 'Whatever.'