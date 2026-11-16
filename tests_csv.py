
import unittest
import os

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


class TestCSV(unittest.TestCase):

    def setUp(self):
        with open("test.csv", "w", encoding="utf-8") as fichier:
            fichier.write("1;Clavier;150\n")
            fichier.write("2;Souris;80\n")

    def tearDown(self):
        if os.path.exists("test.csv"):
            os.remove("test.csv")

    def test_csv_valide(self):
        articles = charger_csv("test.csv")
        self.assertEqual(len(articles), 2)

    def test_fichier_introuvable(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("inexistant.csv")

    def test_ligne_invalide(self):
        with open("test.csv", "w", encoding="utf-8") as fichier:
            fichier.write("1;Clavier\n")

        with self.assertRaises(LigneInvalideException):
            charger_csv("test.csv")

    def test_prix_negatif(self):
        with open("test.csv", "w", encoding="utf-8") as fichier:
            fichier.write("1;Clavier;-150\n")

        with self.assertRaises(PrixNegatifException):
            charger_csv("test.csv")


if __name__ == "__main__":
    unittest.main()
