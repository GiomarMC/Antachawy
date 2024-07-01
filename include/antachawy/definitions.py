class LexemasAntachawy:
    QHAPAQ = "qhapaq"                           # Programa
    YUPAY = "yupay"                             # int
    CHUNKAYUQ = "chunkayuq"                     # float
    SANANPA = "sananpa"                         # char
    QAYTU = "qaytu"                             # string
    ASIGNA = "="                                # =
    ARI = "ari"                                 # if
    MANA_CHAYQA_ARI = "mana chayqa ari"         # else if
    MANA_CHAYQA = "mana chayqa"                 # else
    SIQIY = "Siqiy"                             # print
    IMAPAQ = "imapaq"                           # for
    CHAYKAMA = "chaykama"                       # while
    LLAVE_IZQ = "{"                             # {
    LLAVE_DER = "}"                             # }
    PAREN_IZQ = "("                             # (
    PAREN_DER = ")"                             # )
    COMA = ","                                  # ,
    MAS = "+"                                   # +
    MENOS = "-"                                 # -
    MULTIPLICA = "*"                            # *
    DIVIDE = "/"                                # /
    MAYOR = ">"                                 # >
    MENOR = "<"                                 # <
    IGUAL = "=="                                # ==
    DIFERENTE = "!="                            # !=
    MAYOR_IGUAL = ">="                          # >=
    MENOR_IGUAL = "<="                          # <=
    NUMERO = "NUMERO"                           # numero
    CADENA = "CADENA"                           # cadena
    ID = "ID"                                   # identificador

class EtiquetasAntachawy:
    TIPO = "TIPO"
    ASIGNACION = "ASIGNACION"
    CONDICION = "CONDICION"
    OPERADOR_ARITMETICO = "OPERADOR_ARITMETICO"
    OPERADOR_RACIONAL = "OPERADOR_RACIONAL"
    IMPRESION = "IMPRESION"
    BUCLE_FOR = "BUCLE_FOR"
    BUCLE_WHILE = "BUCLE_WHILE"
    BLOQUE = "BLOQUE"
    PROGRAMA = "PROGRAMA"
    NUMERO = "NUMERO"
    CADENA = "CADENA"
    ID = "ID"

lexema_a_etiqueta = {
    LexemasAntachawy.QHAPAQ: EtiquetasAntachawy.PROGRAMA,
    LexemasAntachawy.YUPAY: EtiquetasAntachawy.TIPO,
    LexemasAntachawy.CHUNKAYUQ: EtiquetasAntachawy.TIPO,
    LexemasAntachawy.SANANPA: EtiquetasAntachawy.TIPO,
    LexemasAntachawy.QAYTU: EtiquetasAntachawy.TIPO,
    LexemasAntachawy.ASIGNA: EtiquetasAntachawy.ASIGNACION,
    LexemasAntachawy.ARI: EtiquetasAntachawy.CONDICION,
    LexemasAntachawy.MANA_CHAYQA_ARI: EtiquetasAntachawy.CONDICION,
    LexemasAntachawy.MANA_CHAYQA: EtiquetasAntachawy.CONDICION,
    LexemasAntachawy.SIQIY: EtiquetasAntachawy.IMPRESION,
    LexemasAntachawy.IMAPAQ: EtiquetasAntachawy.BUCLE_FOR,
    LexemasAntachawy.CHAYKAMA: EtiquetasAntachawy.BUCLE_WHILE,
    LexemasAntachawy.LLAVE_IZQ: EtiquetasAntachawy.BLOQUE,
    LexemasAntachawy.LLAVE_DER: EtiquetasAntachawy.BLOQUE,
    LexemasAntachawy.PAREN_IZQ: EtiquetasAntachawy.BLOQUE,
    LexemasAntachawy.PAREN_DER: EtiquetasAntachawy.BLOQUE,
    LexemasAntachawy.COMA: EtiquetasAntachawy.BLOQUE,
    LexemasAntachawy.MAS: EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.MENOS: EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.MULTIPLICA: EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.DIVIDE: EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.MAYOR: EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.MENOR: EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.IGUAL: EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.DIFERENTE: EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.MAYOR_IGUAL: EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.MENOR_IGUAL: EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.NUMERO: EtiquetasAntachawy.NUMERO,
    LexemasAntachawy.CADENA: EtiquetasAntachawy.CADENA,
    LexemasAntachawy.ID: EtiquetasAntachawy.ID
}

simbolos_compuestos = {
    "!": LexemasAntachawy.ASIGNA,
    LexemasAntachawy.ASIGNA: LexemasAntachawy.ASIGNA,
    LexemasAntachawy.MAYOR: LexemasAntachawy.ASIGNA,
    LexemasAntachawy.MENOR: LexemasAntachawy.ASIGNA,
}

primeros = {
    "Programa": [LexemasAntachawy.QHAPAQ],
    "ListaDefiniciones": [LexemasAntachawy.QHAPAQ],
    "Definicion": [LexemasAntachawy.QHAPAQ],
    "Bloque": [LexemasAntachawy.LLAVE_IZQ,LexemasAntachawy.LLAVE_DER, LexemasAntachawy.SIQIY, LexemasAntachawy.ARI, LexemasAntachawy.MANA_CHAYQA_ARI, LexemasAntachawy.MANA_CHAYQA, LexemasAntachawy.IMAPAQ, LexemasAntachawy.CHAYKAMA],
    "ListaCondiciones": [LexemasAntachawy.ARI, LexemasAntachawy.MANA_CHAYQA_ARI, LexemasAntachawy.MANA_CHAYQA],
    "Condiciones": [LexemasAntachawy.ARI, LexemasAntachawy.MANA_CHAYQA_ARI, LexemasAntachawy.MANA_CHAYQA, LexemasAntachawy.IMAPAQ, LexemasAntachawy.CHAYKAMA],
    "CondicionesElseif": [LexemasAntachawy.MANA_CHAYQA_ARI],
    "CondicionElseif": [LexemasAntachawy.MANA_CHAYQA_ARI],
    "CondicionElse": [LexemasAntachawy.MANA_CHAYQA],
    "Declaraciones": [LexemasAntachawy.YUPAY, LexemasAntachawy.CHUNKAYUQ, LexemasAntachawy.SANANPA, LexemasAntachawy.QAYTU],
    "Declaracion": [LexemasAntachawy.YUPAY, LexemasAntachawy.CHUNKAYUQ, LexemasAntachawy.SANANPA, LexemasAntachawy.QAYTU],
    "Operaciones": [LexemasAntachawy.ID],
    "Operacion": [LexemasAntachawy.ID],
    "Asignacion": [LexemasAntachawy.ID],
    "Condicion": [LexemasAntachawy.ID, LexemasAntachawy.NUMERO, LexemasAntachawy.CADENA],
    "Operador": [LexemasAntachawy.MAS, LexemasAntachawy.MENOS, LexemasAntachawy.MULTIPLICA, LexemasAntachawy.DIVIDE],
    "OperadorRelacional": [LexemasAntachawy.MAYOR, LexemasAntachawy.MENOR, LexemasAntachawy.IGUAL, LexemasAntachawy.DIFERENTE, LexemasAntachawy.MAYOR_IGUAL, LexemasAntachawy.MENOR_IGUAL],
    "Tipo": [LexemasAntachawy.YUPAY, LexemasAntachawy.CHUNKAYUQ, LexemasAntachawy.SANANPA, LexemasAntachawy.QAYTU],
    "Expresion": [LexemasAntachawy.ID, LexemasAntachawy.NUMERO, LexemasAntachawy.CADENA],
}

producciones = {
    "Programa": ["ListaDefiniciones", "ListaCondiciones"],
    "ListaDefiniciones": [["Definicion", "ListaDefiniciones"], ["Definicion"]],
    "Definicion": [[LexemasAntachawy.QHAPAQ, LexemasAntachawy.PAREN_IZQ, LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER], [LexemasAntachawy.QHAPAQ, LexemasAntachawy.PAREN_IZQ, LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, LexemasAntachawy.LLAVE_DER]],
    "Bloque": [["ListaCondiciones"], ["Declaraciones"], ["Operaciones"], [LexemasAntachawy.SIQIY, LexemasAntachawy.PAREN_IZQ, "Expresion", LexemasAntachawy.PAREN_DER]],
    "ListaCondiciones": [["Condiciones", "ListaCondiciones"], ["Condiciones"]],
    "Condiciones": [
        [LexemasAntachawy.ARI, LexemasAntachawy.PAREN_IZQ, "Condicion", LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER, "CondicionesElseif", "CondicionElse"], 
        [LexemasAntachawy.ARI, LexemasAntachawy.PAREN_IZQ, "Condicion", LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER, "CondicionElse"], 
        [LexemasAntachawy.ARI, LexemasAntachawy.PAREN_IZQ, "Condicion", LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER], 
        ["cicloFor"], 
        ["cicloWhile"]],
    "CondicionesElseif": [["CondicionElseif", "CondicionesElseif"], ["CondicionElseif"]],
    "CondicionElseif": [LexemasAntachawy.MANA_CHAYQA_ARI, LexemasAntachawy.PAREN_IZQ, "Condicion", LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
    "CondicionElse": [LexemasAntachawy.MANA_CHAYQA, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
    "Declaraciones": [["Declaracion", "Declaraciones"], ["Declaracion"]],
    "Declaracion": [["Tipo", "Asignacion"], ["Tipo", "Expresion"]],
    "Operaciones": [["Operacion", "Operaciones"], ["Operacion"]],
    "Operacion": [LexemasAntachawy.ID, LexemasAntachawy.ASIGNA, LexemasAntachawy.ID, "Operador", LexemasAntachawy.ID],
    "Asignacion": [LexemasAntachawy.ID, LexemasAntachawy.ASIGNA, "Expresion"],
    "Condicion": ["Expresion", "OperadorRelacional", "Expresion"],
    "Operador": [LexemasAntachawy.MAS, LexemasAntachawy.MENOS, LexemasAntachawy.MULTIPLICA, LexemasAntachawy.DIVIDE],
    "OperadorRelacional": [LexemasAntachawy.MAYOR, LexemasAntachawy.MENOR, LexemasAntachawy.IGUAL, LexemasAntachawy.DIFERENTE, LexemasAntachawy.MAYOR_IGUAL, LexemasAntachawy.MENOR_IGUAL],
    "Tipo": [LexemasAntachawy.YUPAY, LexemasAntachawy.CHUNKAYUQ, LexemasAntachawy.SANANPA, LexemasAntachawy.QAYTU],
    "Expresion": [
        ["Expresion", "Operador", "Expresion"], 
        [LexemasAntachawy.ID], 
        [LexemasAntachawy.NUMERO], 
        [LexemasAntachawy.CADENA], 
        ["Expresion", LexemasAntachawy.CADENA, LexemasAntachawy.ID], 
        [LexemasAntachawy.CADENA, LexemasAntachawy.ID]],
}