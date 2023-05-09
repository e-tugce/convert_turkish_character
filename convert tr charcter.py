

text = input("Wriite what you want that may include Turkish characters: ")

def convert_tr(text:str):

    characterSet = {
        "ş": "s",
        "ç": "c",
        "ö":"o",
        "ü":"u",
        "ğ":"g",
        "ı":"i"
    }

    text = list(text.lower())

    for character in text:
        if character in characterSet:
            text[text.index(character)] = characterSet[character]

    return "".join(text)

print(convert_tr(text).capitalize())