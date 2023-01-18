# Soft Desk - Projet #10
__________________________

Le programme a pour objet la création une application permettant de remonter et suivre des problèmes technique.
Un utilisateur peut à ses fins:

- référencer un projet.
- assigner des problèmes à ce projet.
- ajouter des commmentaires à ses problèmes.

______________
HOW TO INSTALL
--------------

Importation des scripts:
---------------------------

Télécharger et extaire le contenu du repertoire https://github.com/Kraynn/P6-SoftDesk dans le répertoire local. 
> 
Puis déplacer le contenu dans le repertoire local voulu.


Ou cloner le répertoire via github en utilisant la commande:
> git clone github.com/Kraynn/P6-SoftDesk


__________________________________________________________
Création de l'environnement virtuel:
------------------------------------
Exectuer les commandes suivantes dans l'invité de commande au sein du répertoire local voulu:
>
>python -m venv softdesk

>softdesk\Scripts\activate.bat

>cd app

>pip install -r requirements.txt

___________________________________________________



Lancer le serveur :
----------------------

A partir de l'environnement virtuel créé, s'assurer d'être dans le fichier "app" puis exécuter la commande suivante:
>
>python manage.py runserver

Les requêtes de l'api se font sur le serveur local à l'adresse suivante:
 > 127.0.0.1:8000


Sur Postmman :
----------------------

L'ensemble des routes de requêtes est documenté sur Postman:
> [Documentation](https://documenter.getpostman.com/view/23482099/2s8ZDVaPAi)

***************************








