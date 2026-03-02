from Enemigo import *
import random
class Zombie(Enemigo):
    def __init__(self, puntos_energia=10, ataque=1):
        super().__init__(Tipos_Enemigos='Zombie', puntos_energia=puntos_energia, ataque=ataque)

    def habla(self):
        print("*Hummmmmm...*")

    def propagar_enfermedad(self):
        print("El Zombie esta tratando de propagar la enfermedad!!")

    def ataque_especial(self):
        print("Zombie taque especial!!")
        funcion_ataque_especial = random.random()<0.50
        if funcion_ataque_especial:
            self.puntos_energia += 2
            print("Zombie ha regenerado su energia con 2HP!")