export type DataType<T> = { new (): T };

export class Serialization {

    /*
    * 
    * Serialize an object to its data type 
    * 
    * Usage:
    *   Serialization.to(Foo, { id: 3, name: 'Fuuuu!'})
    * 
    * Example:   
    *   foo = Serialization.to(Foo, { id: 3, name: 'Fuuuu!'})
    *   
    *   if (foo instanceof Foo) {
    *       return true; 
    *   }
    * 
    * References
    *   https://www.npmjs.com/package/serializer.ts
    *   https://www.typescriptlang.org/docs/handbook/advanced-types.html
    *   http://stackoverflow.com/questions/22885995/how-do-i-initialize-a-typescript-object-with-a-json-object
    *   http://stackoverflow.com/questions/29758765/json-to-typescript-class-instance
    */

    static to<T>(Type: DataType<T>, data: Object): T {
        let obj = new Type();
        Object.keys(data).forEach( key => obj[key] =data[key] );
        return obj;
    }

    /*
    * 
    * Copy all properties from object source to destination 
    * 
    * This function should be used when it is necessary to preserve the object instance type.
    *
    * Usage:
    *   let foo = new Foo();
    *   Serialization.copyFrom(foo, { id: 2, name: 'Foouuu' })
    * 
    */

    static copyFrom<T>(destination: T, source: T ) {
        Object.keys(source).map( key => destination[key] = source[key] )
    }
}

