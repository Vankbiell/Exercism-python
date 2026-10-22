def translate(text):
    vogais = ["a","e","i","o","u"] 
    if (text.startswith("xr") or text.startswith("yt")) or text[0] in vogais:
        return text+"ay"