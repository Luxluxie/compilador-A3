def parser(tokens):
    instrucoes = []
    i = 0
    esperando = "INICIO"

    while i < len(tokens):
        tipo, valor = tokens[i]
        

        if esperando == "INICIO":

            if tipo == "CMD_M":
                esperando = "APOS_M"

            elif tipo == "CMD_G":
                esperando = "APOS_G"

            else:
            
                return None, "Erro sintático: comando inválido"

        elif esperando == "APOS_M":

            if tipo == "DIGITO":
                instrucoes.append(("M", int(valor)))
                esperando = "APOS_COMANDO"
        

            else:
                return None, "Erro sintático: esperado um dígito após M"
        
        elif esperando == "APOS_G":

            if tipo == "DIR":
                instrucoes.append(("G", valor))
                esperando = "APOS_COMANDO"

            else:
                return None, "Erro sintático: esperado uma direção após G"
        
        elif esperando == "APOS_COMANDO":

            if tipo == "VIRGULA":
                esperando = "INICIO"

            elif tipo == "PONTO":
                esperando = "FIM"

            else:
                return None, "Erro sintático: esperado vírgula ou ponto" 
        elif esperando == "FIM":

            return None, "Erro sintático: existem tokens após o ponto final"


        i += 1
    if esperando != "FIM":
        return None, "Erro sintático: faltou o ponto final"

    return instrucoes, None