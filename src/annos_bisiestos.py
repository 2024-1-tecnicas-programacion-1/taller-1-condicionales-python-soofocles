def evaluar(anno):
    if anno % 4 == 0:
        if anno % 100 == 0:
            if anno % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
