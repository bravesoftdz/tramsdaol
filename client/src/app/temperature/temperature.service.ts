import { Injectable } from '@angular/core';
import { Response, Http, Headers, URLSearchParams  } from '@angular/http';

import { ToastrService } from 'toastr-ng2';

import {Observable} from 'rxjs/Observable';

import { environment } from '../../environments/environment';

import { Temperature } from './temperature.model';
import { Serialization } from './temperature.helper';
import { SlimLoadingBarService } from 'ng2-slim-loading-bar';


import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';

@Injectable()
export class TemperatureService {

    private headers = new Headers({
        'Content-Type': 'application/json',
    });

    constructor(private http: Http, private toastrService: ToastrService, 
        private slimLoadingBarService: SlimLoadingBarService) {}

    getByAddress(address: string): Observable<Temperature> {
        this.slimLoadingBarService.start();

        let search = new URLSearchParams();
        search.set('address', address);
        
        let url = `${environment.url}/temperature/`;

        return this.http.get(url, {  search: search, headers: this.headers})
                .map((response: Response) => {
                    this.slimLoadingBarService.complete();
                    return Serialization.to(Temperature, response.json());
                })
                .catch( (error) => {
                    this.slimLoadingBarService.complete();
                    this.toastrService.error('Opsss!', 'An error has occurred!');
                    return this.handleServerError(error)
                })

    }

    private handleServerError(error: Response) {
        return Observable.throw(error.text() || 'Server error');
    }

}

