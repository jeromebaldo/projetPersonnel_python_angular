import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReservChambreComponent } from './reserv-chambre.component';

describe('ReservChambreComponent', () => {
  let component: ReservChambreComponent;
  let fixture: ComponentFixture<ReservChambreComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReservChambreComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ReservChambreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
