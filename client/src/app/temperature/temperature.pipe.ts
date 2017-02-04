import { Pipe, PipeTransform } from '@angular/core';

import { Temperature } from './temperature.model';

/*
 *
 * 
 * Usage:
 *   temperature | label
 * Example:
 *   {{ temperature |  label }}
 *   formats to: Florianópolis, BR
 * 
*/

@Pipe({name: 'label'})
export class LabelPipe implements PipeTransform {
  transform(value: Temperature): string {
      return `${value.city || ''}, ${value.country || ''}`;
  }
}