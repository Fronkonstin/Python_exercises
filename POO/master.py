class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto.")

    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(self.nombre, "ha causado ", damage, " puntos de daño a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, " es de: ", enemigo.vida)
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Rama seca = 3. (2) Pata de elefante = 9. "))
        if opcion == 1:
            self.espada = 3
        elif opcion == 2:
            self.espada = 9
        else:
            print("Opción inválida")

    def atributos(self):
        super().atributos()
        print("-Espada:", self.espada)

    def damage(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self):
        super().atributos()
        print("-Libro:", self.libro)

    def damage(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

#-----------------------------------------------------------
personaje_1 = Personaje("Nano", 20, 10, 4, 100)
personaje_2 = Mago("Chino", 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\n Turno de ", turno)
        print(">> Accion de ", jugador_1.nombre, ":", sep = "")
        jugador_1.atacar(jugador_2)
        print(">> Accion de ", jugador_2.nombre, ":", sep = "")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\n", jugador_1.nombre, " ha ganado")
    elif jugador_2.esta_vivo():
        print("\n", jugador_2.nombre, " ha ganado")
    else:
        print("\nEmpate morrrrrrto")

combate(personaje_1, personaje_2)


