import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";

import { ReservChambreComponent } from "./features/reserv-chambre/reserv-chambre.component";
import { ConstructionComponent } from "./features/construction/construction.component";

const routes: Routes = [
    { path: 'reservation', component: ReservChambreComponent},
    { path: 'construction', component: ConstructionComponent}
  ];

@NgModule({
    imports: [
        RouterModule.forRoot(routes)
    ],
    exports: [
        RouterModule
    ]
})
export class AppRoutingModule{}