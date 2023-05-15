import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header-menu',
  templateUrl: './header-menu.component.html',
  styleUrls: ['./header-menu.component.scss']
})
export class HeaderMenuComponent 
{
  constructor(private router: Router) { }

  onContinue() 
  {
    this.router.navigateByUrl('accueil');
  }
}
