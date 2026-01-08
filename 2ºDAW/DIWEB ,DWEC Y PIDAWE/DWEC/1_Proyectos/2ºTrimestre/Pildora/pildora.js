// ---------------- 2.1.1 Clase ----------------
class Persona {
  #dni; // campo privado

  // ---------------- 2.1.2 Constructor ----------------
  constructor(nombre, edad, dni) {
    this.nombre = nombre;   // propiedad pública
    this._edad = edad;      // controlada con getter/setter
    this.#dni = dni;        // propiedad privada
  }

  // ---------------- 2.1.3 Getters y Setters ----------------
  get edad() {
    return this._edad;
  }
  set edad(valor) {
    if (valor < 0) throw new Error("La edad no puede ser negativa");
    this._edad = valor;
  }
  get dni() {
    return this.#dni;
  }

  // ---------------- 2.1.4 Método ----------------
  saludar() {
    console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años`);
  }

  // ---------------- 2.1.5 Sobrescritura de métodos heredados ----------------
  toString() {
    return `Persona: ${this.nombre}, Edad: ${this.edad}`;
  }
  valueOf() {
    return this.edad;
  }

  // ---------------- 2.1.6 Statics y Abstracts ----------------
  static esMayorDeEdad(edad) {
    return edad >= 18;
  }

  // ---------------- 2.1.7 Campos privados y públicos ----------------
  mostrarCampos() {
    console.log(`Nombre: ${this.nombre}, DNI: ${this.#dni}`);
  }

  // ---------------- 2.1.8 Variables asociadas a objetos ----------------
  asignarHobbies(hobbies) {
    this.hobbies = hobbies;
  }

  // ---------------- 2.1.9 Iteradores y Generadores ----------------
  *[Symbol.iterator]() {
    if (!this.hobbies) return;
    for (const hobby of this.hobbies) yield hobby;
  }

  // ---------------- 2.1.10 Encapsulación y visibilidad ----------------
  getDniSeguro() {
    return `El DNI está protegido: ${this.#dni}`;
  }

  // ---------------- 2.1.11 Métodos asincrónicos ----------------
  async obtenerDatos() {
    return new Promise(resolve => {
      setTimeout(() => resolve(`Datos de ${this.nombre}`), 1000);
    });
  }
}

// ---------------- 2.1.12 Subclases ----------------
class Estudiante extends Persona {
  estudiar() {
    console.log(`${this.nombre} está estudiando`);
  }
}

// ---------------- 2.1.13 Mixins y composición ----------------
const Hablador = Base => class extends Base {
  hablar() { console.log("Estoy hablando..."); }
};
class PersonaHabladora extends Hablador(Persona) {}

// ---------------- 2.1.14 Uso de instanceof y Object.create ----------------
const persona2 = new Persona("Lucía", 18, "98765432B");
console.log(persona2 instanceof Persona); // true

const proto = { hablar() { console.log("Guau"); } };
const perro = Object.create(proto);
perro.hablar(); // Guau

// ---------------- 2.1.15 Métodos especiales de objetos ----------------
const obj = { a: 1 };
console.log(obj.hasOwnProperty("a")); // true

const destino = {};
Object.assign(destino, { x: 1 }, { y: 2 });
console.log(destino); // { x: 1, y: 2 }

const original = { nested: { v: 1 } };
const copia = structuredClone(original);
copia.nested.v = 2;
console.log(original.nested.v); // 1

// ---------------- 2.1.16 Muestra del código ----------------
const persona1 = new Persona("Carlos", 28, "12345678A");
persona1.saludar(); // Hola, soy Carlos y tengo 28 años
console.log(persona1.dni); // 12345678A
console.log(persona1.toString()); // Persona: Carlos, Edad: 28
console.log(+persona1);           // 28
console.log(Persona.esMayorDeEdad(20)); // true

persona1.mostrarCampos(); // Nombre: Carlos, DNI: 12345678A
persona1.asignarHobbies(["leer", "correr"]);
for (const hobby of persona1) console.log(hobby); // leer, correr

console.log(persona1.getDniSeguro()); // El DNI está protegido: 12345678A

persona1.obtenerDatos().then(datos => console.log(datos)); // Datos de Carlos

const estudiante1 = new Estudiante("Ana", 22, "11111111C");
estudiante1.saludar();   // Hola, soy Ana y tengo 22 años
estudiante1.estudiar();  // Ana está estudiando

const personaHabladora = new PersonaHabladora("Luis", 30, "22222222D");
personaHabladora.hablar(); // Estoy hablando...
