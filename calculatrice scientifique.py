import math

while True:
    print("Menu:")
    print("1. Addition/soustraction")
    print("2. Modulo")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Factoriel")
    print("7. Logarithme népérien")
    print("8. Exponentiel")
    print("9. Racine carrée")
    print("0. Quitter")
    choix = input("Veuillez faire votre choix: ")

    if choix == '1':
        nombre_de_termes = 0
        while nombre_de_termes < 2:
            try:
                nombre_de_termes = int(input("Veuillez saisir le nombre de termes (entier): "))
            except ValueError:
                print("Veuillez saisir un nombre entier.")

        somme = 0
        for _ in range(nombre_de_termes):
            terme = float(input("Veuillez saisir le terme: "))
            somme += terme

        print("La somme est ", somme)

    elif choix == '2':
        diviseur = 0
        while diviseur == 0:
            try:
                dividende = float(input("Veuillez saisir le dividende: "))
                diviseur = float(input("Veuillez saisir le diviseur (entier): "))
                if diviseur % 1 != 0:
                    raise ValueError
            except ValueError:
                print("Veuillez saisir un diviseur entier différent de zéro.")

        quotient = dividende // diviseur
        reste = dividende % diviseur
        print("Le reste est ", reste)

    elif choix == '3':
        nombre_de_facteurs = 0
        while nombre_de_facteurs < 2:
            try:
                nombre_de_facteurs = int(input("Veuillez saisir le nombre de facteurs (entier): "))
            except ValueError:
                print("Veuillez saisir un nombre entier.")

            produit = 1
            for _ in range(nombre_de_facteurs):
                facteur = float(input("Veuillez saisir le facteur: "))
                produit *= facteur
        print("Le produit est ", produit)

    elif choix == '4':
        diviseur = 0
        while diviseur == 0:
            try:
                dividende = float(input("Veuillez saisir le dividende: "))
                diviseur = float(input("Veuillez saisir le diviseur (entier différent de zéro): "))
                if diviseur % 1 != 0 or diviseur == 0:
                    raise ValueError
            except ValueError:
                print("Veuillez saisir un diviseur entier différent de zéro.")

        resultat = dividende / diviseur
        print("Le résultat est ", resultat)

    elif choix == '5':
        base = float(input("Veuillez saisir la base: "))
        exposant = int(input("Veuillez saisir l'exposant (entier): "))
        resultat = base ** exposant
        print("Le résultat est ", resultat)

    elif choix == '6':
        n = 0
        while n <= 0:
            try:
                n = int(input("Veuillez saisir un nombre (entier positif): "))
                if n <= 0:
                    raise ValueError
            except ValueError:
                print("Veuillez saisir un nombre entier positif.")

        factoriel = 1
        for i in range(1, n + 1):
            factoriel *= i

        print("Le factoriel est ", factoriel)

    elif choix == '7':
        x = 0
        while x <= 0:
            try:
                x = float(input("Veuillez saisir un réel (positif): "))
                if x <= 0:
                    raise ValueError
            except ValueError:
                print("Veuillez saisir un réel positif.")

        n = 10
        somme = 0
        for i in range(1, n + 1):
            somme += ((x - 1) / x) / i

        print("Le logarithme népérien de ", x, " est ", somme)

    elif choix == '8':
        x = float(input("Veuillez saisir un nombre: "))
        n = 10
        resultat = 1
        terme = 1
        for _ in range(1, n + 1):
            terme *= (x / _)
            resultat += terme

        print("L'exponentiel de ", x, " est ", resultat)

    elif choix == '9':
        n = -1
        while n < 0:
            try:
                n = int(input("Veuillez saisir un nombre (entier positif): "))
                if n < 0:
                    raise ValueError
            except ValueError:
                print("Veuillez saisir un nombre entier positif.")

        precision = 0.00001
        x = n
        while abs(x * x - n) > precision:
            x = (x + n / x) / 2

        print("La racine carrée de ", n, " est ", x)

    elif choix == '0':
        print("Au revoir!")
        break

    else:
        print("Choix invalide, veuillez réessayer.")
    # Demander à l'utilisateur s'il souhaite continuer
    continuer = input("Voulez-vous continuer? (oui/non) ").lower()
    if continuer != "oui":
        print("Au revoir!")
        break
