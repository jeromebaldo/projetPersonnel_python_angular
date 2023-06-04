# projetPersonnel_python_angular

## Contexte et objectifs de l'application 
Réalisé dans le cadre de la matière "Projet Personnel" au sein de l'UQAC. 

L'objectif de cette matière est d'explorer une technologie ou un concept de manière individuel sous la supervision d'un professeur. 

Dans ce cadre, j'ai découvert angular ainsi que le concept d'application full-stack. 

## Point de situation
Les couches sont composées : 

- python flask pour le back-end 
- angular pour le front-end 
- PostgreSQL

## Installation et exécution de l'application

Prérequis pour le run de l'application 
### Logiciels
- Docker
- terminal de commande windows ou terminal dans 
### Etapes
- télécharger le dossier
- dans un terminal de commandes, se positionner dans le répertoire du fichier docker-compose.yml 
- taper la commande docker-compose up
### Accès aux différentes composantes
- Pour la partie cliente => ouvrir un navigateur à l'adresse suivante => localhost:4200/
- Pour accèder à PGAdmin => ouvrir le navigateur à l'addresse suivante => localhost:80/
- Pour accèder à la partie serveur => utiliser le logiciel postman pour dialoguer à l'adresse http://127.0.0.1:5000, attention l'applciation possède des contraintes de méthodes et/ou de json à recevoir. 
### Couper l'application et supprimer le montage des conteneurs dans Docker
- crtl + c dans le terminal actif 
- tapez la commande docker-compose down pour effacer les montages 
- effacer les volumes crées en allant dans le logiciel Docker

## Sources
## Changelog
### V1 => 
- version initiale
### V1.1 => 
- rajout de méthode pour le client dans la partie serveur
- angular mis sous docker et inclus dans le docker-compose 
### V1.2 => 
- correction pour le chemin get /clientHisto dans le serveur , traitement du cas si pas existance du client


