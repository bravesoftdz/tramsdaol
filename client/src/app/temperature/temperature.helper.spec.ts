import { Serialization } from './temperature.helper';


describe('Helper: Temperature', () => {

    it('should return the correct instante when serialization object', () => {
        
        class Foo {
            id: number;
            name: string;
        }

        let foo = Serialization.to(Foo, { id: 1, name: 'Fooooo!' })
        
        expect(foo.constructor.name).toBe('Foo');
        
        expect(foo.id).toBe(1);
        expect(foo.name).toBe('Fooooo!');
    });

});