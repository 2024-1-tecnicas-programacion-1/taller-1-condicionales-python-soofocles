def evaluar(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    respuesta = ""

    if residuo == 0:
        respuesta = "La división es exacta.\n"
    else:
        respuesta = "La división no es exacta.\n"
    
    respuesta += f"Cociente: {cociente}\n"
    respuesta += f"Residuo: {residuo}"
    return respuesta
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
