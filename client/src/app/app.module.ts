import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { TemperatureCardComponent } from './temperature/temperature-card.component';
import { AddressSearchComponent } from './temperature/address-search.component';

import { LabelPipe } from './temperature/temperature.pipe';

import { TemperatureService } from './temperature/temperature.service';

@NgModule({
  declarations: [
    AppComponent,
    TemperatureCardComponent,
    AddressSearchComponent,

    LabelPipe,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
  ],
  providers: [
    TemperatureService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
