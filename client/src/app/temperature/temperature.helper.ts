export type DataType<T> = { new (): T };

export class Serialization {
    static to<T>(Type: DataType<T>, data: Object): T {
        let obj = new Type();
        Object.keys(data).forEach( key => obj[key] =data[key] );
        return obj;
    }
}
