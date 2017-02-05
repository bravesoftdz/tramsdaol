import { Pipe, PipeTransform } from '@angular/core';

import { Temperature } from './temperature.model';

/*
 * Format to display the country and city of the current temperature
 * 
 * Usage:
 *   temperature | label
 * Example:
 *   {{ temperature |  label }}
 *   formats to: Florianópolis, BR
 * 
*/

@Pipe({ name: 'label' })
export class LabelPipe implements PipeTransform {
  transform(value: Temperature): string {
    if (value instanceof Temperature) {
        return `${value.city || 'Without a city'}, ${value.country ||  'Without a country'}`;
    };

    throw new Error('Requires a object type Temperature as input');
    
  }
}