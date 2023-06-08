import { Component} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-histo-client',
  templateUrl: './histo-client.component.html',
  styleUrls: ['./histo-client.component.scss']
})
export class HistoClientComponent 
{
  
  nom: string = '';
  prenom: string = '';
  InfoClient: any = {};

  ValiderFormulaire() {
    // Vous pouvez ajouter ici la logique pour envoyer les données du formulaire au serveur et récupérer les informations du client correspondant
    // Par exemple, vous pouvez appeler une API avec les valeurs nom et prenom pour obtenir les informations du client

    // Une fois que vous avez les informations du client, vous pouvez les assigner à la variable InfoClient
    
    // Exemple de code fictif pour assigner des informations au client
    this.InfoClient = {
      nom: 'Dupont',
      prenom: 'John',
      // Ajoutez d'autres informations du client ici
    };
    console.log(this.InfoClient);
  }
}
