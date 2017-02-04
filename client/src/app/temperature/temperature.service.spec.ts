import { Serialization } from './temperature.helper';
import { Temperature } from './temperature.model';
import { TemperatureService } from './temperature.service';
import { async, inject, TestBed } from '@angular/core/testing';
import { BaseRequestOptions, Http, HttpModule, Response, ResponseOptions, ResponseType } from '@angular/http';
import { MockBackend } from '@angular/http/testing';

class MockError extends Response implements Error {
    name: any
    message: any
}

describe('Service: Temperature', () => {
    beforeEach(() => {

        TestBed.configureTestingModule({
            providers: [
                TemperatureService,

                MockBackend,
                BaseRequestOptions,
                {
                    provide: Http,
                    useFactory: (backend, options) => new Http(backend, options),
                    deps: [MockBackend, BaseRequestOptions]
                }
            ],
            imports: [
                HttpModule
            ]
        });
    });

    it('should construct', async(inject(
        [TemperatureService, MockBackend], (service, mockBackend) => {
            expect(service).toBeDefined();
        })));

    describe('getByAddress', () => {

        it('should return error response', async(inject(
            [TemperatureService, MockBackend], (service, mockBackend) => {

                mockBackend.connections.subscribe(conn => {

                    let responseOpts = new ResponseOptions( 
                        {   type: ResponseType.Error, 
                            status: 404, 
                            body: 'Opsss',
                        } 
                    );
                    conn.mockError(new MockError(responseOpts));

                });

                const result = service.getByAddress('Mondai, BR');

                result.subscribe(
                    res => { },
                    error => {
                        expect(error).toBe('Opsss');                        
                    });
            })));

        it('should parse response', async(inject(
            [TemperatureService, MockBackend], (service, mockBackend) => {

                mockBackend.connections.subscribe(conn => {
                    conn.mockRespond(new Response(new ResponseOptions({
                        body: JSON.stringify(
                            {
                                'country': 'BR',
                                'city': 'Mondai',
                                'degrees': 78.98,
                            }
                        )
                    })));
                });

                const result = service.getByAddress('Mondai, BR');

                result.subscribe(res => {
                    expect(res).toEqual(
                        Serialization.to(Temperature,
                            {
                                'country': 'BR',
                                'city': 'Mondai',
                                'degrees': 78.98,
                            }
                        ));
                });
            })));
    });
});
