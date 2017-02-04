import { Component, Input } from '@angular/core';

import { Temperature } from './temperature.model';

@Component({
  selector: 'app-temperature-card',
  templateUrl: './temperature-card.component.html',
})

export class TemperatureCardComponent {

  @Input() temperature: Temperature;

}
