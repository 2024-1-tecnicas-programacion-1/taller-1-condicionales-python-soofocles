def evaluar(num_victorias_a, num_victorias_b):
 
    if (num_victorias_a - num_victorias_b > 2) or (num_victorias_a < 0) or (num_victorias_b < 0) or (num_victorias_a > 7) or (num_victorias_b > 7):
        return "El resultado es inválido"
    elif (num_victorias_a >= 6 and num_victorias_a - num_victorias_b >= 2) or (num_victorias_a == 7 and num_victorias_b == 6):
        # Si el jugador A ha ganado al menos 6 juegos y tiene al menos 2 juegos más que el jugador B o si el jugador A ha ganado 7 partidos es el ganador
        return "El ganador es el jugador A"
    elif (num_victorias_b >= 6 and num_victorias_b - num_victorias_a >= 2) or (num_victorias_b == 7 and num_victorias_a == 6):
        # Si el jugador B ha ganado al menos 6 juegos y tiene al menos 2 juegos más que el jugador A o si el jugador B ha ganado 7 partidos es el ganador
        return "El ganador es el jugador B"
    else:
        # Si ninguna de las condiciones anteriores se cumple el set todavía no termina
        return "El set todavía no termina"
    return ""

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
