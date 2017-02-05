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

    it('should return false if city and country was not defined)', () => {
        let temperature = new Temperature();
        temperature.degrees = 102.01;
        temperature.unit = TEMPERATURE_UNIT.Celsius;

        expect(temperature.hasCity).toBe(false);
    });

    it('should return true if city and country was defined)', () => {
        let temperature = new Temperature();
        temperature.city = 'Barra Bonita';
        temperature.country = 'BR';
        temperature.degrees = 102.01;
        temperature.unit = TEMPERATURE_UNIT.Celsius;

        expect(temperature.hasCity).toBe(true);
    });

    it('should return false if city was not defined)', () => {
        let temperature = new Temperature();
        temperature.degrees = 102.01;
        temperature.country = 'BR';
        temperature.unit = TEMPERATURE_UNIT.Celsius;

        expect(temperature.hasCity).toBe(false);
    });


});
