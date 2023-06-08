import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistoClientComponent } from './histo-client.component';

describe('HistoClientComponent', () => {
  let component: HistoClientComponent;
  let fixture: ComponentFixture<HistoClientComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HistoClientComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HistoClientComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
