#include <iostream>
#include <string>
#include <map>

using namespace std;

bool verifier_entree(int entree, int min, int max) {
    if (entree < min || entree > max) {
        return false;
    }
    return true;
}

string determiner_signe(int jour, int mois) {
    map<string, pair<int, int>> correspondances = {
        //dates au format mois-jour
        {"Verseau", {120, 218}},  // 20 janvier - 18 février
        {"Poisson", {219, 320}},  // 19 février - 20 mars
        {"Bélier", {321, 419}},   // 21 mars - 19 avril
        {"Taureau", {420, 520}},  // 20 avril - 20 mai
        {"Gémeaux", {521, 620}},  // 21 mai - 20 juin
        {"Cancer", {621, 722}},   // 21 juin - 22 juillet
        {"Lion", {723, 822}},     // 23 juillet - 22 août
        {"Vierge", {823, 922}},   // 23 août - 22 septembre
        {"Balance", {923, 1022}}, // 23 septembre - 22 octobre
        {"Scorpion", {1023, 1121}},  // 23 octobre - 21 novembre
        {"Sagittaire", {1122, 1221}}, // 22 novembre - 21 décembre
        {"Capricorne", {1222, 119}}   // 22 décembre - 19 janvier
    };

    int date = mois * 100 + jour;
    for (auto &signe : correspondances) {
        if (date >= signe.second.first && date <= signe.second.second) {
            return signe.first;
        }
    }
    return "None";
}

int main() {
    while (true) {
        cout << "Veuillez saisir votre date de naissance\n";
        int jour, mois, annee;
        cout << "Jour : ";
        cin >> jour;
        if (!verifier_entree(jour, 1, 31)) {
            cout << "Erreur, les jours sont entre 1 et au plus 31.\n";
            continue;
        }
        cout << "Mois : ";
        cin >> mois;
        if (!verifier_entree(mois, 1, 12)) {
            cout << "Erreur, les mois sont entre 1 et 12.\n";
            continue;
        }
        cout << "Année : ";
        cin >> annee;
        if (!verifier_entree(annee, 1800, 2099)) {
            cout << "Erreur, l’année doit être supérieure strictement à 1800.\n";
            continue;
        }
        string signe = determiner_signe(jour, mois);
        cout << "Votre signe astrologique est : " << signe << "\n";
        string continuer;
        cout << "Voulez vous continuer ? (oui/non) : ";
        cin >> continuer;
        if (continuer != "oui") {
            cout << "\n Au revoir !\n";
            break;
        }
    }
    return 0;
}
