import { Component, OnInit } from '@angular/core';

import { DispoChambreService } from '../../core/services/dispo_chambre_service';
import { DispoChambre } from '../../core/modeles/dispo_chambre_model';

@Component({
  selector: 'app-reserv-chambre',
  templateUrl: './reserv-chambre.component.html',
  styleUrls: ['./reserv-chambre.component.scss']
})
export class ReservChambreComponent implements OnInit
{
  listChambreDispo: DispoChambre[] = [];
  selectedType: string = '';

  constructor(private dispoChambre: DispoChambreService) {}

  ngOnInit() 
  {
    this.listChambreDispo = this.dispoChambre.Get_dispoChambre("tous");
  }

  ValiderChoix(): void 
  {
    this.listChambreDispo = this.dispoChambre.Get_dispoChambre(this.selectedType);
    console.log(this.selectedType);
  }
}
