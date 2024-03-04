def estPremier(nombre):
    if nombre < 2:
        return False
    for i in range(2, nombre):
        if (nombre % i) == 0:
            return False
    return True

compteur = 0
nombre = 0
while compteur < 10:
    if estPremier(nombre):
        print(nombre)
        compteur += 1
    nombre += 1
    
