# Rapprochement de Virements / Factures — Streamlit App

Cette application Streamlit permet de trouver **toutes les combinaisons possibles de montants** issues d'une liste donnée (virements) qui s'approchent d'une somme cible (facture) avec une tolérance paramétrable.

---

## Fonctionnalités principales

* Saisie interactive des montants de virements (format décimal avec espace comme séparateur).
* Saisie de la somme cible à atteindre.
* Recherche exhaustive de toutes les combinaisons de virements dont la somme est égale à la cible dans une petite marge de tolérance (0,01 € par défaut).
* Affichage clair des combinaisons possibles.
* Gestion des erreurs de saisie.

---

## Comment ça marche ?

1. **Saisie des données** :

   * Entrez une liste de montants séparés par des espaces (ex : `100.25 50.00 23.75`)
   * Entrez la somme cible (ex : `150.00`)

2. **Recherche** :
   L’algorithme trie la liste, élimine les doublons inutiles et explore toutes les combinaisons possibles (backtracking) pour trouver celles qui s’approchent de la cible avec une tolérance fixée à 0,01 €.

3. **Résultats** :
   Affichage de toutes les combinaisons trouvées qui respectent la condition.

---

## Installation

1. Assurez-vous d'avoir Python 3.x installé.

2. Installez Streamlit si ce n’est pas déjà fait :

```bash
pip install streamlit
```

3. Placez le fichier Python de l’application (`Combi_VIRT_FACT_GUI.py` par exemple) dans un dossier.

---

## Lancement de l'application

Dans un terminal, exécutez :

```bash
streamlit run /chemin/vers/Combi_VIRT_FACT_GUI.py
```

Remplacez `/chemin/vers/Combi_VIRT_FACT_GUI.py` par le chemin réel de votre fichier.

---

## Structure du code

* `trouver_combinaisons(virements, cible, tolerance=0.01)` : fonction principale qui utilise une approche **backtracking** pour générer toutes les combinaisons possibles.
* Interface Streamlit :

  * Titre et explications
  * Zones de saisie pour les montants et la cible
  * Bouton pour lancer la recherche
  * Affichage des résultats ou des messages d’erreur

---

## Points d’amélioration possibles

* Ajouter une option pour modifier la tolérance.
* Permettre d’importer les montants depuis un fichier CSV.
* Optimiser la recherche pour gérer de plus grands ensembles de données.
* Ajouter la possibilité d’exporter les résultats.

---

## Remarques

* Le calcul peut devenir lent si la liste des virements est trop longue ou si beaucoup de combinaisons sont possibles.
* L’algorithme ignore les montants supérieurs à la cible pour optimiser la recherche.

---

## Exemple d’utilisation

1. Entrer :

```
100.25 50.00 23.75 75.00
```

2. Cible :

```
150.00
```

3. Cliquer sur **Lancer la recherche**
4. Obtenir les combinaisons trouvées, par exemple :

* 100.25 + 50.00 = 150.00 €
* 75.00 + 75.00 = 150.00 €
