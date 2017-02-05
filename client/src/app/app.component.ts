import { Component } from '@angular/core';
import { Temperature } from './temperature/temperature.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})

export class AppComponent { 

    temperature: Temperature = new Temperature();

}
