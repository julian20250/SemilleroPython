# -*- coding: utf-8 -*-
class Soldado:
    """
    posX: posición en el eje x
    posY: posición en el eje y
    direction: dirección en la que se moverá la unidad
    1=arriba, 2=derecha, 3=abajo, 4=izquierda
    hp: puntos de vida
    vel: velocidad
    alc: alcance
    damage: daño
    band: bando (1,2)
    """
    def __init__(self, posX, posY,direction, hp, vel, alc, damage, band):
        self.posX=posX
        self.posY=posY
        self.direction=direction
        self.hp=hp
        self.vel=vel
        self.alc=alc
        self.damage=damage
        self.band=band

    def printMyself(self):
        "Método para imprimir los datos del objeto"
        return ', '.join("%s: %s" % item for item in vars(self).items())

    def moveMyself(self):
        "Método para moverse dependiendo de la dirección"
        if(direction==1):
            self.posY+=1
        elif(direction==2):
            self.posX+=1
        elif(direction==3):
            self.posY-=1
        elif(direction==4):
            self.posX-=1

class Infantry(Soldado):
    def __init__(self, posX,posY, direction,band):
        Soldado.__init__(self,posX,posY,direction,50,5,3,20,band)

class Artillery(Soldado):
    """
    reloading: tiempo de recarga
    """
    def __init__(self,posX,posY,direction,band):
        self.reloading=3
        Soldado.__init__(self,posX,posY,direction,200,2,20,50,band)

class Support(Soldado):
    def __init__(self, posX, posY,direction, band):
        Soldado.__init__(self,posX,posY,direction,30,10,3,30,band)

def startUp(primeraArmada, segundaArmada, boundaries):
    "Ubico unidades de infantería en los límites, en dos columnas"
    for x in range(2):
        for y in range(boundaries):
            primeraArmada.append(Infantry(x,y,2,1))

    for x in range(boundaries-2, boundaries):
        for y in range(boundaries):
            segundaArmada.append(Infantry(x,y,4,2))

def moveAll(primeraArmada, segundaArmada):
    """
    Muevo a las tropas a la derecha e izquierda; en caso de encontrarse
    con los límites del mapa, dan media vuelta para volver a atacar sus 
    enemigos
    """
    
def printSoldiers(Armada):
    for x in Armada:
        print(x.printMyself())
