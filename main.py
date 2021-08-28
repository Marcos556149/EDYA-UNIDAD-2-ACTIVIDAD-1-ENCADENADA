from ClasePila import Pila
if __name__=='__main__':
    unaPila= Pila()
    unaPila.insertar(20)
    unaPila.insertar(3)
    unaPila.insertar(22)
    unaPila.insertar(12)
    unaPila.insertar(17)
    unaPila.insertar(0)
    unaPila.mostrar()
    print("Suprimamos el ultimo elemento de la pila: ",unaPila.suprimir())
    print("Pila luego de suprimir el ultimo elemento")
    unaPila.mostrar()


