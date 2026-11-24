def lexer (texto: str) -> list[tuple[str, str]]:
    tokens = []

    for n in texto:
        if n == ' ':
            continue    
        elif n == 'M': 
            tokens.append(("CMD_M", "M"))
        elif n == 'G': 
            tokens.append(("CMD_G", "G"))
        elif n in "12345":
            tokens.append(("DIGITO", n))
        elif n in "DET":
            tokens.append(("DIR", n))
        elif n == ',': 
            tokens.append(("VIRGULA", n))
        elif n == '.': 
            tokens.append(("PONTO", n))
        else:
            tokens.append(("ERRO", n))
    
    return tokens


if __name__ == "__main__":
    entrada = input ("escreva seu comando")
    resultado = lexer(entrada)
    for token in resultado:
        print(token)