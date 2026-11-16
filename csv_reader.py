
import csv
import os


class CsvException(Exception):
    pass


class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):
    if not os.path.isfile(chemin):
        raise FichierIntrouvableException("Fichier CSV introuvable.")

    articles = []

    with open(chemin, "r", encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier, delimiter=";")

        for numero, ligne in enumerate(lecteur, start=1):
            if not ligne or all(colonne.strip() == "" for colonne in ligne):
                continue

            if len(ligne) != 3:
                raise LigneInvalideException(
                    f"Ligne {numero} : exactement 3 colonnes sont attendues."
                )

            identifiant, nom, prix = [colonne.strip() for colonne in ligne]

            if not identifiant or not nom:
                raise LigneInvalideException(
                    f"Ligne {numero} : identifiant ou nom manquant."
                )

            try:
                prix = float(prix)
            except ValueError:
                raise LigneInvalideException(
                    f"Ligne {numero} : le prix doit être numérique."
                )

            if prix <= 0:
                raise PrixNegatifException(
                    f"Ligne {numero} : le prix doit être positif."
                )

            articles.append({
                "id": identifiant,
                "nom": nom,
                "prix": prix
            })

    return articles
