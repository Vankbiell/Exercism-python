
def translate(text):

    vogais = ["a","e","i","o","u"] 

    if (text.startswith("xr") or text.startswith("yt")) or text[0] in vogais:
        return text + "ay"

    if not text[0] in vogais and not text[1] in vogais and not text[2] in vogais:
        return text[3:] + text[0:3] + "ay"

    if not text[0] in vogais and not text[1] in vogais:
        return text[2:] + text[0:2] + "ay"
    
    if not text[0] in vogais:
        return text[1:] + text[0] + "ay"

print(translate("Pig"))