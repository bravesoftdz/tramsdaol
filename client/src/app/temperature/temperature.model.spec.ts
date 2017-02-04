import { Temperature, TEMPERATURE_UNIT } from './temperature.model';

describe('Model: Temperature', () => {

    it('should return the temperture formated in degrees Fahrenheit (auto init property "unit")', () => {
        let temperature = new Temperature();
        temperature.city = 'Florianópolis';
        temperature.country = 'BR';
        temperature.degrees = 102.01;

        expect(temperature.do).toBe('102.01° F');
    });

    it('should return the null temperature (auto init property "unit")', () => {
        let temperature = new Temperature();
        temperature.city = 'Barra Bonita';
        temperature.country = 'BR';
        temperature.degrees = 102.01;
        temperature.unit = TEMPERATURE_UNIT.Celsius;

        expect(temperature.do).toBe(null);
    });

});
