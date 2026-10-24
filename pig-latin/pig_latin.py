"""Pig Latin"""


def translate(text):
    """Traduz um texto do inglês para Pig Latin."""
    # Se o texto tiver espaços (mais do que uma palavra), traduz palavra a palavra
    if " " in text:
        return " ".join(translate(palavra) for palavra in text.split())

    # Vetor de vogais para usar nas validações.
    vogais = ["a", "e", "i", "o", "u"]

    if text[1] == "y" or text[2] == "y":
        if text[1] == "y":
            return text[1:] + text[0] + "ay"
        return text[2:] + text[0:2] + "ay"

    # Se o texto começar com "qu"
    if text.startswith("qu"):
        return text[2:] + text[0:2] + "ay"

    # Se o texto começar com uma consoante e logo a seguir ter "qu".
    if text[0] not in vogais and text[1] == "q" and text[2] == "u":
        return text[3:] + text[0:3] + "ay"

    # Se o texto começar com (xr, yt ou vogais).
    if (text.startswith("xr") or text.startswith("yt")) or text[0] in vogais:
        return text + "ay"

    # Se o texto na posição 1, 2 e 3 não começarem com vogais.
    if text[0] not in vogais and text[1] not in vogais and text[2] not in vogais:
        return text[3:] + text[0:3] + "ay"

    # Se o texto na posição 1 e 2 não começarem com vogais.
    if text[0] not in vogais and text[1] not in vogais:
        return text[2:] + text[0:2] + "ay"

    # Retorno padrão (quando começa apenas com 1 consoante):
    return text[1:] + text[0] + "ay"