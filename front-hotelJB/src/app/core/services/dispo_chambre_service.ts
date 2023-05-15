import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { DispoChambre } from '../modeles/dispo_chambre_model';


@Injectable({ providedIn: 'root' })

export class DispoChambreService {

  constructor(private http: HttpClient) { }

  Get_dispoChambre(typeDeChambre: string): DispoChambre[]
  {
    //definition de l'entete de la requete 
    const httpOptions = {
        headers: new HttpHeaders({
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': 'http://localhost:4200'
        })
    };
    
    //definition de l'url de la requete
    let url = 'http://localhost:5000/dispoChambre/' + typeDeChambre;
   
    //execution de la requete
    let chambreDispo: DispoChambre[] = [];
    
    this.http.get(url, httpOptions).subscribe(
        response => 
        { 
          const list = Object.values(response);
          //console.log(list[0]);
          
          for (let i = 0; i < list[0].length; i++) 
          {
            const element = list[0][i];
            
            const chambre: DispoChambre = {
              numeroChambre: element.numeroChambre,
              typeDeChambre: element.typeDeChambre,
              literie: element.literie,
              rangement: element.rangement,
              sanitaire: element.sanitaire
            };
  
            chambreDispo.push(chambre);
          }                         
        }, 
        error => {console.log(error);});
    
    return chambreDispo;
  }
}

