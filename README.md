[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
# Django-Test-Project

Ce projet a été implémenté dans le but de s'entrainer aux différentes formes de tests. Le code source contient un projet Django qui un mini site e-commerce. Vous pourrez ainsi développer l'ensemble des scénarios nécessaires afin de tester l'ensemble du code source. À noter que des propositions de corrections sont mises à disposition dans différentes branches du répertoire.

## Pré-requis

* Installer Python 3 : [Téléchargement Python 3](https://www.python.org/downloads/)
* Installer git : [Téléchargement Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Installation

### 1. Télécharger le projet sur votre répertoire local : 
```
git clone git@github.com:OpenClassrooms-Student-Center/4425126-testing-python-django.git 
cd 4425126-testing-python-django
```
### 2. Mettre en place un environnement virtuel :
* Créer l'environnement virtuel: `python -m venv venv`
* Activer l'environnement virtuel :
    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`
    
### 3. Installer les dépendances du projet
```
pip install -r requirements.txt
```

## Démarrage
* Lancer le serveur à l'aide de la commande suivante : 
`python manage.py runserver`

## Corrections
1. Proposition de correction pour les tests unitaires avec UnitTest :
```
git checkout unittest-test
python -m unittest discover tests/
```

2. Proposition de correction pour les tests unitaires avec Pytest :
```
git checkout pytest-test
pytest tests/
```
