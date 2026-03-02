from Enemigo import *
import random 

class Ogro(Enemigo):
    def __init__(self, puntos_energia=28, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("Ogro aplastar todo!!!")

    def ataque_especial(self):
        print("Ogro taque especial!!")
        funcion_ataque_especial = random.random()<0.50
        if funcion_ataque_especial:
            self.puntos_energia += 4
            print("Ogro enojado y incremento su ataque por 4!")