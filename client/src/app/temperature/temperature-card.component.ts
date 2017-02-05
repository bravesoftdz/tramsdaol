import { Component, Input } from '@angular/core';

import { Temperature } from './temperature.model';

@Component({
  selector: 'app-temperature-card',
  templateUrl: './temperature-card.component.html',
  styles: [`
    .sebm-google-map-container {
       height: 300px;
     }
  `],
})

export class TemperatureCardComponent {

  @Input() temperature: Temperature;

}
