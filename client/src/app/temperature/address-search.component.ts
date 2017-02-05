import { ToastrService } from 'toastr-ng2';
import { Serialization } from './temperature.helper';
import { Component, Input } from '@angular/core';

import { TemperatureService } from './temperature.service';
import { Temperature } from './temperature.model';

@Component({
  selector: 'app-address-search',
  templateUrl: './address-search.component.html',
})
export class AddressSearchComponent {

  @Input() temperature: Temperature;

  constructor(private temperatureService: TemperatureService, private toastrService: ToastrService) { }

  findTemperature(address: string) {

    if (address === '') {
      this.toastrService.info('Uhun', 'You need to put an address :-)')
    } else {
      this.temperatureService.getByAddress(address)
        .subscribe(temperature => Serialization.copyFrom(this.temperature, temperature), error => console.log(error))
    }
  }

}
