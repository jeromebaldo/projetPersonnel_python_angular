from peewee import *
import os
from peewee import Model, PostgresqlDatabase, AutoField, CharField, IntegerField, FloatField, BooleanField
import click
from flask.cli import with_appcontext
from playhouse.postgres_ext import *


class BaseModel(Model):
    class Meta:
        database = PostgresqlDatabase(
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT']
        )
#classe et table chambre 
class typechambre(BaseModel):
    typeDeChambre = CharField(primary_key=True)
    literie = CharField()
    rangement = CharField()
    sanitaire = CharField()

#classe et table chambre 
class chambre(BaseModel):
    numChambre = IntegerField(primary_key=True)
    typeChambre = ForeignKeyField(typechambre, backref='chambres')

#classe et table client
class client(BaseModel):
    idClient = AutoField(primary_key=True)
    nom = CharField()
    prenom = CharField()
    date_naissance = DateField()
    adresse_postale = CharField()
    telephone = CharField()
    mail = CharField()
    moyen_paiement = CharField()

class reservation(BaseModel):
    numReser = AutoField(primary_key=True)
    idClient = ForeignKeyField(client, backref='reservations')
    numChambr = ForeignKeyField(chambre, backref='reservations')
    dateDebutReserv = DateField()
    nbrNuit = IntegerField()
    prixNuit = FloatField()
    prixTotal = FloatField()

#remplissage de la table typechambre
def rempli_typeChambre():
        
        # données à insérer dans la table TypeChambre
        typesChambre = [
            {'typeDeChambre': '1p', 'literie': 'lit simple', 'rangement': 'armoire', 'sanitaire': 'douche'},
            {'typeDeChambre': '2p_LS', 'literie': '2 lits simples', 'rangement': 'armoire', 'sanitaire': 'douche'},
            {'typeDeChambre': '2p_LD', 'literie': '1 lit 2 places', 'rangement': 'armoire', 'sanitaire': 'douche'},
            {'typeDeChambre': '4p_DO_LD_LS', 'literie': '1 lit 2 places, 2 lits simples', 'rangement': '2 armoires', 'sanitaire': 'douche à l’italienne'},
            {'typeDeChambre': '4p_BA_LS', 'literie': '4 lits simples', 'rangement': '2 armoires', 'sanitaire': 'baignoire'},
            {'typeDeChambre': 'delux', 'literie': '1 lit 2 places', 'rangement': '3 armoires, 1 bureau', 'sanitaire': 'baignoire, douche à l’italienne'},
        ]
        
        for chambre in typesChambre:
            typechambre.create(**chambre)

#remplissage de la table chambre
def rempli_chambre():

    #chambres 1 personne 
    type_chambre = typechambre.get(typechambre.typeDeChambre == '1p')
    for i in range(1, 12):
        chambre.create(numChambre=i,typeChambre=type_chambre)
    #chambres 2 personnes / 2 lits simples
    type_chambre = typechambre.get(typechambre.typeDeChambre == '2p_LS')
    for i in range(12, 14):
        chambre.create(numChambre=i,typeChambre=type_chambre)
    #chambres 2 personnes / 1 lit double 
    type_chambre = typechambre.get(typechambre.typeDeChambre == '2p_LD')
    for i in range(14, 21):
        chambre.create(numChambre=i,typeChambre=type_chambre)
    #chambres 4 personnes / baignoire et lits simples 
    type_chambre = typechambre.get(typechambre.typeDeChambre == '4p_BA_LS')
    for i in range(21, 23):
        chambre.create(numChambre=i,typeChambre=type_chambre)  
    #chambres 4 personnes / douche + lit double + lits simples 
    type_chambre = typechambre.get(typechambre.typeDeChambre == '4p_DO_LD_LS')
    for i in range(23, 26):
        chambre.create(numChambre=i,typeChambre=type_chambre) 
    #chambres delux 
    type_chambre = typechambre.get(typechambre.typeDeChambre == 'delux')
    for i in range(26, 28):
        chambre.create(numChambre=i,typeChambre=type_chambre) 

#remplissage de la table client 
def rempli_client():
    clients = [
        {'nom': 'Dupont', 'prenom': 'Jean', 'date_naissance': '1980-05-12', 'adresse_postale': '1 Rue de la Paix, 75001 Paris', 'telephone': '+33 6 12 34 56 78', 'mail': 'jean.dupont@email.com', 'moyen_paiement': 'Carte bancaire'},
        {'nom': 'Martin', 'prenom': 'Sophie', 'date_naissance': '1995-07-25', 'adresse_postale': '10 Rue des Fleurs, 69001 Lyon', 'telephone': '+33 6 23 45 67 89', 'mail': 'sophie.martin@email.com', 'moyen_paiement': 'Virement bancaire'},
        {'nom': 'Durand', 'prenom': 'Pierre', 'date_naissance': '1972-02-15', 'adresse_postale': '15 Rue des Champs, 31000 Toulouse', 'telephone': '+33 6 34 56 78 90', 'mail': 'pierre.durand@email.com', 'moyen_paiement': 'Carte bancaire'},
        {'nom': 'Lefèvre', 'prenom': 'Julie', 'date_naissance': '1988-12-04', 'adresse_postale': '20 Rue du Moulin, 59000 Lille', 'telephone': '+33 6 45 67 89 01', 'mail': 'julie.lefevre@email.com', 'moyen_paiement': 'Chèque'},
        {'nom': 'Garcia', 'prenom': 'Antoine', 'date_naissance': '1999-09-01', 'adresse_postale': '25 Rue du Soleil, 13001 Marseille', 'telephone': '+33 6 56 78 90 12', 'mail': 'antoine.garcia@email.com', 'moyen_paiement': 'PayPal'},
        {'nom': 'Michel', 'prenom': 'Céline', 'date_naissance': '1985-03-08', 'adresse_postale': '30 Rue des Écoles, 44000 Nantes', 'telephone': '+33 6 67 89 01 23', 'mail': 'celine.michel@email.com', 'moyen_paiement': 'Carte bancaire'},
        {'nom': 'Roux', 'prenom': 'Mathieu', 'date_naissance': '1990-11-18', 'adresse_postale': '35 Rue du Commerce, 69002 Lyon', 'telephone': '+33 6 78 90 12 34', 'mail': 'mathieu.roux@email.com', 'moyen_paiement': 'Carte bancaire'},       
        {'nom': 'Fournier', 'prenom': 'Marie', 'date_naissance': '1997-06-22', 'adresse_postale': '40 Rue de la Liberté, 33000 Bordeaux', 'telephone': '+33 6 90 12 34 56', 'mail': 'marie.fournier@email.com', 'moyen_paiement': 'Virement bancaire'},
        {'nom': 'Lemoine', 'prenom': 'Alexandre', 'date_naissance': '1982-09-28', 'adresse_postale': '45 Rue de la Gare, 75002 Paris', 'telephone': '+33 6 12 34 56 78', 'mail': 'alexandre.lemoine@email.com', 'moyen_paiement': 'Chèque'},
        {'nom': 'Girard', 'prenom': 'Aurélie', 'date_naissance': '1993-04-11', 'adresse_postale': '50 Rue des Roses, 69003 Lyon', 'telephone': '+33 6 12 34 56 78', 'mail': 'aurelie.girard@email.com', 'moyen_paiement': 'Carte bancaire'},
    ]

    for client_ligne in clients:
            client.create(**client_ligne)

#remplissage de la table reservation
def rempli_reservation():
    
    #1er client
    clientReserv = client.get(client.idClient == 1)
    chambreReserv = chambre.get(chambre.numChambre == 8)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-14', nbrNuit= 3, prixNuit= 25, prixTotal= 75.4)
    #2e client
    clientReserv = client.get(client.idClient == 2)
    chambreReserv = chambre.get(chambre.numChambre == 2)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-14', nbrNuit= 2, prixNuit= 30, prixTotal= 60)
    #3e client
    clientReserv = client.get(client.idClient == 3)
    chambreReserv = chambre.get(chambre.numChambre == 3)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-15', nbrNuit= 1, prixNuit= 40, prixTotal= 40)
    #4e client
    clientReserv = client.get(client.idClient == 4)
    chambreReserv = chambre.get(chambre.numChambre == 4)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-15', nbrNuit= 4, prixNuit= 20, prixTotal= 80.8)
    #5e client
    clientReserv = client.get(client.idClient == 5)
    chambreReserv = chambre.get(chambre.numChambre == 5)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-16', nbrNuit= 2, prixNuit= 30, prixTotal= 60)
    #6e client
    clientReserv = client.get(client.idClient == 6)
    chambreReserv = chambre.get(chambre.numChambre == 6)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-16', nbrNuit= 1, prixNuit= 40, prixTotal= 40)    
    #7e client
    clientReserv = client.get(client.idClient == 7)
    chambreReserv = chambre.get(chambre.numChambre == 7)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-17', nbrNuit= 3, prixNuit= 24, prixTotal= 75.4)
    #8e client
    clientReserv = client.get(client.idClient == 8)
    chambreReserv = chambre.get(chambre.numChambre == 25)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-17', nbrNuit= 2, prixNuit= 30, prixTotal= 60)
    #9e client
    clientReserv = client.get(client.idClient == 9)
    chambreReserv = chambre.get(chambre.numChambre == 26)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-18', nbrNuit= 1, prixNuit= 40, prixTotal= 40)
    #10e client
    clientReserv = client.get(client.idClient == 10)
    chambreReserv = chambre.get(chambre.numChambre == 27)
    reservation.create(idClient= clientReserv,numChambr= chambreReserv, dateDebutReserv= '2023-03-18', nbrNuit= 4, prixNuit= 20, prixTotal= 80.8)

@click.command("init-db")
@with_appcontext  
def init_db_command():
    
    database = PostgresqlDatabase(
    database=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
    port=os.environ['DB_PORT']
    )

    if not database.table_exists('typechambre') or not database.table_exists('chambre') or not database.table_exists('client') or not database.table_exists('reservation'):
        
        database.create_tables([typechambre, chambre, client, reservation])
        click.echo("OK - INITIALISATION BDD")
    
        #remplissage des tables avec les données de jeux  
        rempli_typeChambre()
        click.echo("OK - REMPLISSAGE TABLE typechambre")
        rempli_chambre()
        click.echo("OK - REMPLISSAGE TABLE chambre")
        rempli_client()
        click.echo("OK - REMPLISSAGE TABLE client")
        rempli_reservation()
        click.echo("OK - REMPLISSAGE TABLE reservation")
    
    else:
        click.echo("OK - INIT + REMPLISSAGE DEJA FAIT")

def init_app(app):
    app.cli.add_command(init_db_command)