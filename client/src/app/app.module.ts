import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AgmCoreModule } from 'angular2-google-maps/core';
import { ToastrModule } from 'toastr-ng2';
import { SlimLoadingBarModule } from 'ng2-slim-loading-bar';

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

    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyBDkk7pWJpjlXwviCYyUnuBG4_jyUgVrVQ'
    }),
    ToastrModule.forRoot(),
    SlimLoadingBarModule.forRoot(),
  ],
  providers: [
    TemperatureService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
