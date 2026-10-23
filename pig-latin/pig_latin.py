"""Pig Latin"""
def translate(text):
    # Vetor de vogais para usar nas validações.
    vogais = ["a","e","i","o","u"] 

    # Se o texto começar com (xr, yt ou vogais).
    if (text.startswith("xr") or text.startswith("yt")) or text[0] in vogais:
        # Então ele retorna o texto mais "ay".
        return text + "ay"

    # Se o texto começar com "qu"
    if text.startswith("qu") or (not text[0] in vogais and text[1] == "q" and text[2] == "u"):
        # Então retorna o texto depois da posição 2 mais o texto da posição 0 até a 2 junto do "ay".
        return text[2:] + text[0:2] + "ay"
    
    # Se o texto na posição 1, 2 e 3 não começarem com vogais.
    if not text[0] in vogais and not text[1] in vogais and not text[2] in vogais:
        # Então retorna o texto depois da posição 3 mais texto da posição 0 até a 3 junto do "ay".
        return text[3:] + text[0:3] + "ay"

    # Se o texto na posição 1 e 2 não começarem com vogais.
    if not text[0] in vogais and not text[1] in vogais:
        # Então retorna o texto depois da posição 2 mais o texto da posição 0 até a 2 junto do "ay".
        return text[2:] + text[0:2] + "ay"

    # Se o texto na posição 1 não começar com vogais.
    if not text[0] in vogais:
        #Então retorna o texto a partir da posição 1 mais o texto da posição 0 junto do "ay".
        return text[1:] + text[0] + "ay"
    

print(translate("square"))