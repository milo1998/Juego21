from random import sample

class Game():
        ganador="jugador"
        def __init__(self, jugador, talla, baraja):
                self.jugador = jugador
                self.talla = talla
                self.baraja = baraja

        def entregaTalla(self,jugador,talla,baraja):
                if(suma(jugador)>suma(talla)):
                    return self.entregaTalla(jugador,talla+[entrega(baraja)],baraja[1:])
                else:
                    if(suma(talla)<=21 and suma(talla)>=suma(jugador)):
                        print("")
                        print(">> Jugador >>")
                        print(jugador)
                        print("")
                        print(">> Talla >>")
                        print(talla)
                        print("")
                        print("La casa gana!")
                        self.ganador="talla"
                        return baraja
                        print("")
                        print("------------------------------------------")
                    else:
                        print("")
                        print(">> Jugador >>")
                        print(jugador)
                        print("")
                        print(">> Talla >>")
                        print(talla)
                        print("")
                        print("Usted ha ganado!")
                        self.ganador="jugador"
                        return baraja
                        print("")
                        print("------------------------------------------")

        def repartirCartas(self, jugador, talla, baraja):
                self.jugador = jugador
                self.talla = talla
                if(len(self.jugador)==0):      
                        self.jugador = entregaBaraja(jugador, self.baraja)
                        self.baraja= self.baraja[3:]
                        self.talla = entregaBaraja(talla, self.baraja)
                        self.baraja= self.baraja[3:]
                        print(">> Jugador >>")
                        print(self.jugador)
                        print("")
                        print(">> Talla >>")
                        print(self.talla[1:])
                        print("")
                        print("------------------------------------------")


        def game(self, jugador, talla, baraja):
                self.jugador = jugador
                self.talla = talla
                
                while True:
                        if ((input("Carta o se planta >> ")=='1') and (suma(self.jugador)<=21)):
                                self.jugador = self.jugador +[entrega(self.baraja)]
                                print(self.jugador)
                                self.baraja= self.baraja[2:]
                        else:
                                break
                if(suma(self.jugador)<=21):
                        return self.entregaTalla(self.jugador,self.talla,self.baraja)
                else:
                        print("")
                        print(">> Talla >>")
                        print(self.talla)
                        print("")
                        print("La casa Gana!")
                        return self.talla
                        self.ganador="talla"

def entregaBaraja(jugador, baraja):
        if(len(jugador)<=1):
                return entregaBaraja(jugador+[entrega(baraja)],baraja[2:])
        else:
                return jugador
        
        
def contador(lista):
        lista1 = []
        lista1 = lista
        if(len(lista1)==0):
                return 0
        else:
                if(identificador(lista1[0])=='J' or identificador(lista1[0])=='Q' or identificador(lista1[0])=='K'):
                        return contador(lista1[1:])+10
                if(identificador(lista1[0])=='A'):
                        return contador(lista1[1:])+1
                else:
                        return contador(lista1[1:])+ identificador(lista1[0])
def suma(lista1):
        lista = []
        lista = lista1
        if(len(lista)==0):
                return 0
        if(contador(lista)>11):
                return contador(lista)
        else:
                if(identificador(lista[0])=='A'):
                        return contador(lista)+10
                else:
                        if(identificador(lista[0])=='J' or identificador(lista[0])=='Q' or identificador(lista[0])=='K'):
                                return suma(lista[1:])+10
                        else:
                                return suma(lista[1:])+ identificador(lista[0])
def identificador(lista):
        return lista[0]

#Llena la lista con las 52 cartas y desordena la baraja
def llenado():
        return sample([(x, y) for x in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in ['Picas', 'Corazones', 'Diamantes', 'Treboles']], 52)

#retorna 2 cartas si la lista esta vacia y despues solo una
def entrega(baraja):
        return baraja[0]




game1 = Game([],[],[])
game1.baraja=llenado()
game1.repartirCartas([],[],game1.baraja)
game1.game(game1.jugador,game1.talla,game1.baraja)
