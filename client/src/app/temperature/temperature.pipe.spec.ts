import { Temperature } from './temperature.model';
import { LabelPipe } from './temperature.pipe';

import {
    inject, TestBed,
} from '@angular/core/testing';

describe('Pipe: LabelPipe', () => {
    let pipe;

    beforeEach(() => TestBed.configureTestingModule({
        providers: [LabelPipe]
    }));

    it('should return a label of the temperature', inject([LabelPipe], (pipe) => {

        let temperature = new Temperature();
        temperature.city = 'São Miguel do Oeste';
        temperature.country = 'BR';

        expect( pipe.transform(temperature) ) .toBe('São Miguel do Oeste, BR');
    }));

    it('should return a label without city', inject([LabelPipe], (pipe) => {

        let temperature = new Temperature();
        temperature.country = 'BR';

        expect( pipe.transform(temperature) ) .toBe('Without a city, BR');
    }));

    it('should return a label without country', inject([LabelPipe], (pipe) => {

        let temperature = new Temperature();
        temperature.city = 'São Miguel do Oeste';
        expect( pipe.transform(temperature) ) .toBe('São Miguel do Oeste, Without a country');
    }));

    it('should throw if instance not an instance of the Temperature', inject([LabelPipe], (pipe) => {
        expect( () => pipe.transform({}).toThrow());
    }));

    it('should throw if not used with a "null" instance', inject([LabelPipe], (pipe) => {
        expect(() => pipe.transform(null)).toThrow();
    }));

    it('should throw if not used with a "undefined" instance' , inject([LabelPipe], (pipe) => {
        expect(() => pipe.transform(undefined)).toThrow();
    }));


}) 