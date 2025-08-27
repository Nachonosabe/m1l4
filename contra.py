importar aleatorio
def gen_pass(longitud_de_paso):
    elementos = "+-/*!&$#?=@<>"
    contraseña = ""
    para i en rango(longitud_de_paso):
        contraseña += random.choice(elementos)
    devolver contraseña

