import { Injectable } from '@angular/core';
import { Response, Http, Headers, URLSearchParams  } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import {Observable} from 'rxjs/Observable';

import { environment } from '../../environments/environment';

import { Temperature } from './temperature.model';
import { Serialization } from './temperature.helper';

import 'rxjs/add/observable/throw';

@Injectable()
export class TemperatureService {

    private headers = new Headers({
        'Content-Type': 'application/json',
    });

    constructor(private http: Http) {}

    getByAddress(address: string): Observable<Temperature> {

        let search = new URLSearchParams();
        search.set('address', address);
        
        let url = `${environment.url}/temperature/`;

        return this.http.get(url, {  search: search, headers: this.headers})
                .map((response: Response) => {
                    return Serialization.to(Temperature, response.json());
                })    
                .catch(this.handleServerError)
    }

    private handleServerError(error: Response) {
        return Observable.throw(error.text() || 'Server error');
    }

}
