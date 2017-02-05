import { Component, Input } from '@angular/core';

import { Temperature } from './temperature.model';

@Component({
  selector: 'app-temperature-card',
  templateUrl: './temperature-card.component.html',
  styles: [`
    .booticon-lg {
      width: 144px;
      height: 144px;
      font-size: 80px;
      line-height: 140px;
  }
  `]
})

export class TemperatureCardComponent {

  @Input() temperature: Temperature;

}
