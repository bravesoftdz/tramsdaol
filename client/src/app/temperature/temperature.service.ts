import { Injectable } from '@angular/core';
import { Http, Headers, URLSearchParams  } from '@angular/http';

import { Temperature } from './temperature.model';
import { Serialization } from './temperature.helper';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class TemperatureService {

    private headers = new Headers({
        'Content-Type': 'application/json',
    });

    constructor(private http: Http) {}

    getByAddress(address: string): Promise<Temperature> {

        let search = new URLSearchParams();
        search.set('address', address);

        let url = 'http://127.0.0.1:8000/api/temperature/';

        return this.http.get(url, {  search: search, headers: this.headers})
               .toPromise()
               .then(response => Serialization.to(Temperature, response.json()))
               .catch(this.showError);
    }

    private showError(error: any): Promise<any> {
        console.error('An error occurred', error);
        return Promise.reject(error.message || error);
    }

}
