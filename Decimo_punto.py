Velocidad_Luz: float = 2,998e+8
Velocidad_Sonido: float = 343
Velocidad_Carro: float = 147.5
Velocidad_Bolt: float = 11.667

if __name__ == "__main__" :
    Distancia : int = int(input("Dijite una distancia en metros: "))
    if Distancia >= 0 :
        Tiempo_Luz = Distancia/(Velocidad_Luz)
        Tiempo_Sonido = Distancia/(Velocidad_Sonido)
        Tiempo_Carro = Distancia/(Velocidad_Carro)
        Tiempo_Bolt = Distancia/(Velocidad_Bolt)
        print("La luz recorre esa distancia en "+ str(Tiempo_Luz))
        print("El sonido recorre esa distancia en "+ str(Tiempo_Luz))
        print("El carro recorre esa distancia en "+ str(Tiempo_Carro))
        print("Usain Bolt recorre esa distancia en "+ str(Tiempo_Bolt))
    else:
        print("Dijite una medida positiva para poder medirla")