def evaluar(caracter):
    if caracter.isalpha():
        # Verificar si es una letra
        if caracter.isupper():
            return "Es una letra mayúscula."
        else:
            return "Es una letra minúscula."
    elif caracter.isdigit():
        # Verificar si es un número
        return "Es un número."
    else:
        # Si no es ni una letra ni un número
        return "No es ni una letra ni un número."

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
