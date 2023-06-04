from flask import Flask, jsonify, request
from flask_cors import CORS
from peewee import *

from serveur_hotel_jb.models.models import init_app, typechambre, chambre, reservation, client


def create_app(initial_config=None):
    
    app = Flask("serveur_hotel_jb")
    CORS(app)

    init_app(app) 

    @app.route('/dispoChambre/<string:type_chambre>', methods=['GET'])
    def get_dispo_total(type_chambre):
        
        #verification du type de chambres
        if type_chambre == "tous":
            chambres_dispo = chambre.select().where(~(chambre.numChambre << reservation.select(reservation.numChambr)))
        else:
            chambres_dispo = chambre.select().where(chambre.typeChambre == type_chambre, 
                                          ~(chambre.numChambre << reservation.select(reservation.numChambr)))

        #recuperation des chambres disponibles   
        list_dispos = []
        
        for chambres in chambres_dispo:
            chambre_ligne = {
                "numeroChambre": chambres.numChambre,
                "typeDeChambre": chambres.typeChambre.typeDeChambre,
                "literie": chambres.typeChambre.literie,
                "rangement": chambres.typeChambre.rangement,
                "sanitaire": chambres.typeChambre.sanitaire
            }
            list_dispos.append(chambre_ligne)
        
        return jsonify({'dispo': list_dispos}), 200


    @app.route('/clientHisto', methods=['GET'])
    def get_client_histo():
        client_recherch = request.get_json()

        try:
            client_trouv = client.get((client.nom == client_recherch['client']['nom']) & (client.prenom == client_recherch['client']['prenom']))
        
            client_final = [
                {"nom": client_trouv.nom},
                {"prenom": client_trouv.prenom},
                {"date_naissance": client_trouv.date_naissance},
                {"adresse_postale": client_trouv.adresse_postale},
                {"telephone": client_trouv.telephone},
                {"mail": client_trouv.mail},
                {"moyen_paiement": client_trouv.moyen_paiement}
            ]
        
            return jsonify({'client': client_final}), 200

        except DoesNotExist:
            return jsonify({'error': 'Le client n\'existe pas'}), 404


    return app




