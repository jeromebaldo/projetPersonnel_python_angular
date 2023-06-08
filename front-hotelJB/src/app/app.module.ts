import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import { HeaderMenuComponent } from './core/header-menu/header-menu.component';
import { ReservChambreComponent } from './features/reserv-chambre/reserv-chambre.component';
import { AppRoutingModule } from './app-routing.module';
import { ConstructionComponent } from './features/construction/construction.component';
import { HistoClientComponent } from './features/histo-client/histo-client.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderMenuComponent,
    ReservChambreComponent,
    ConstructionComponent,
    HistoClientComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }