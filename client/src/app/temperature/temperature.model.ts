export enum TEMPERATURE_UNIT {
    Celsius = 1,
    Fahrenheit,
}

export class Temperature {
    country: string;
    city: string;
    degrees: number;

    unit: TEMPERATURE_UNIT =  TEMPERATURE_UNIT.Fahrenheit;

    get do(): string{
        switch (this.unit) {
            case TEMPERATURE_UNIT.Fahrenheit:
                return `${this.degrees}° F`
            default:
                return null;
        }
  
    }
}