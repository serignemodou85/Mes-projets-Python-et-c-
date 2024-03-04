 import heapq

def dijkstra(G, P, N, indice_depart):
    INFINI = 10000  # Définir une valeur infinie pour initialiser les distances
    D = [INFINI]*N  # Initialiser toutes les distances à l'infini
    predecesseur = [None]*N  # Initialiser tous les prédécesseurs à None
    D[indice_depart] = 0  # La distance de la source à elle-même est 0

    queue = [(0, indice_depart)]  # Initialiser la file de priorité avec la source
    while queue:  # Tant que la file de priorité n'est pas vide
        (dist, actuel) = heapq.heappop(queue)  # Obtenir le sommet avec la plus petite distance
        if dist != D[actuel]:  # Si la plus petite distance n'est pas égale à la distance actuelle, passer au prochain sommet
            continue

        for voisin in range(N):  # Pour chaque voisin du sommet actuel
            ancienne_distance = D[voisin]  # Obtenir l'ancienne distance du voisin
            nouvelle_distance = D[actuel] + P[actuel][voisin]  # Calculer la nouvelle distance du voisin
            if nouvelle_distance < ancienne_distance:  # Si la nouvelle distance est plus petite que l'ancienne distance
                D[voisin] = nouvelle_distance  # Mettre à jour la distance du voisin
                predecesseur[voisin] = actuel  # Mettre à jour le prédécesseur du voisin
                heapq.heappush(queue, (nouvelle_distance, voisin))  # Ajouter le voisin à la file de priorité

    return D, predecesseur  # Retourner les distances et les prédécesseurs

def main():
    INFINI = 10000  # Définir une valeur infinie pour initialiser les poids des arêtes
    while True:
        try:
            N = int(input("Entrez le nombre de noeud : "))  # Demander à l'utilisateur d'entrer le nombre de sommets
            if N < 0:  # Si le nombre de sommets est négatif
                print("Le nombre de noeud doit être un entier positif.")  # Afficher un message d'erreur
            else:
                break  # Sinon, sortir de la boucle
        except ValueError:  # Si l'utilisateur n'entre pas un nombre entier
            print("Veuillez entrer un nombre entier.")  # Afficher un message d'erreur

    G = {}  # Initialiser le graphe
    P = [[INFINI] * N for _ in range(N)]  # Initialiser la matrice des poids avec des valeurs infinies
    for i in range(N):  # Pour chaque sommet
        sommet = input(f"Entrez le nom du noeud {i + 1} : ")  # Demander à l'utilisateur d'entrer le nom du sommet
        while sommet in G:  # Si le sommet existe déjà
            print("Ce noeud existe déjà. Veuillez entrer un nouveau nom.")  # Afficher un message d'erreur
            sommet = input(f"Entrez le nom du noeud {i + 1} : ")  # Demander à l'utilisateur d'entrer un nouveau nom de sommet
        G[sommet] = i  # Ajouter le sommet au graphe

    for i in range(N):  # Pour chaque paire de sommets
        for j in range(N):
            while True:
                try:
                    poids = int(input(f"Entrez le poids de l'arête entre le noeud {i + 1} et le noeud {j + 1} : "))  # Demander à l'utilisateur d'entrer le poids de l'arête
                    if poids < 0:  # Si le poids est négatif
                        print("Le poids doit être un entier positif.")  # Afficher un message d'erreur
                    else:
                        P[i][j] = poids if poids != 0 else INFINI  # Mettre à jour le poids de l'arête dans la matrice des poids
                        break  # Sortir de la boucle
                except ValueError:  # Si l'utilisateur n'entre pas un nombre entier
                    print("Veuillez entrer un nombre entier.")  # Afficher un message d'erreur

    while True:
        S1 = input("Entrez la source : ")  # Demander à l'utilisateur d'entrer la source
        if S1 in G:  # Si la source existe dans le graphe
            break  # Sortir de la boucle
        else:
            print("Ce noeud n'existe pas. Veuillez entrer un noeud valide.")  # Sinon, afficher un message d'erreur

    indice_depart = G[S1]  # Obtenir l'indice de la source
    D, predecesseur = dijkstra(G, P, N, indice_depart)  # Exécuter l'algorithme de Dijkstra
     
    for nom_sommet, i in G.items():  # Pour chaque sommet du graphe
        chemin = []  # Initialiser le chemin
        j = i
        while j is not None:  # Tant que le prédécesseur existe
            chemin.append(list(G.keys())[j])  # Ajouter le nom du sommet au chemin
            j = predecesseur[j]  # Passer au prédécesseur
        chemin.reverse()  # Inverser le chemin
        print(f"Le chemin le plus court du noeud {S1} au noeud {nom_sommet} est {chemin} avec une distance de {D[i]}.")  # Afficher le chemin le plus court et la distance

if __name__ == "__main__":
    main()  # Exécuter la fonction principale
