def formatear_cadena(texto, longitud_maxima):
    if len(texto.split()) > longitud_maxima:
        #print(cadena[:10]+"...")
        texto_nuevo = texto.split()[:10]
        return " ".join(texto_nuevo) + "..."

texto = "Esta es un texto muy largo que necesita ser acortado usando ..."
longitud_maxima = 10
texto_formateado = formatear_cadena(texto, longitud_maxima)
print(texto_formateado)