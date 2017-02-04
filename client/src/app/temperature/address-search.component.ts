import { Component } from '@angular/core';

import { TemperatureService } from './temperature.service';
import { Temperature } from './temperature.model';

@Component({
  selector: 'app-address-search',
  templateUrl: './address-search.component.html',
})
export class AddressSearchComponent {

  temperature: Temperature = new Temperature();

  constructor(private temperatureService: TemperatureService) { }

  findTemperature(address: string) {
    this.temperatureService.getByAddress(address)
      .subscribe(temperature => this.temperature = temperature, error => console.log(error))
  }

}
