def verifier_entree(entree, min, max):
    """
    Vérifie si l'entree est un nombre entier et si elle est comprise entre min et max.
    """
    try:
        entier = int(entree)
    except ValueError:
        return False, "Erreur, la valeur doit être un nombre entier."
    if entier < min or entier > max:
        return False, f"Erreur, la valeur doit être comprise entre {min} et {max}."
    return True, ""

def determiner_signe(jour, mois):
    """
    Détermine le signe astrologique associé à la date de naissance.
    """
    correspondances = {
        "Verseau": ((1, 20), (2, 18)),
        "Poisson": ((2, 19), (3, 20)),
        "Bélier": ((3, 21), (4, 19)),
        "Taureau": ((4, 20), (5, 20)),
        "Gémeaux": ((5, 21), (6, 20)),
        "Cancer": ((6, 21), (7, 22)),
        "Lion": ((7, 23), (8, 22)),
        "Vierge": ((8, 23), (9, 22)),
        "Balance": ((9, 23), (10, 22)),
        "Scorpion": ((10, 23), (11, 21)),
        "Sagittaire": ((11, 22), (12, 21)),
        "Capricorne": ((12, 22), (1, 19))
    }
    for signe, ((debut_mois, debut_jour), (fin_mois, fin_jour)) in correspondances.items():
        if (mois == debut_mois and jour >= debut_jour) or (mois == fin_mois and jour <= fin_jour):
            return signe
    return None

def main():
    """
    Programme principal.
    """
    while True:
        print("Veuillez saisir votre date de naissance")
        jour = input("Jour : ")
        valide_jour, message_jour = verifier_entree(jour, 1, 31)
        if not valide_jour:
            print(message_jour)
            continue
        mois = input("Mois : ")
        valide_mois, message_mois = verifier_entree(mois, 1, 12)
        if not valide_mois:
            print(message_mois)
            continue
        annee = input("Année : ")
        valide_annee, message_annee = verifier_entree(annee, 1800, 2099)
        if not valide_annee:
            print(message_annee)
            continue
        signe = determiner_signe(int(jour), int(mois))
        print("Votre signe astrologique est :", signe)
        continuer = input("Voulez vous continuer ? (oui/non) : ")
        if continuer.lower() != "oui":
            print("Fin du programme\nAu revoir !")
            break

if __name__ == "__main__":
    main()
