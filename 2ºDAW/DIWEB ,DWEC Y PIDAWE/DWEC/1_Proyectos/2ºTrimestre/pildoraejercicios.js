/*PÍLDORA DWEC – EJERCICIOS PROPUESTOS
 Programación Orientada a Objetos en JavaScript*/

/* =============================================
   EJERCICIO PROPUESTO 1
   Clase Coche
   ============================================= */
class Coche {
  constructor(marca, modelo) {
    this.marca = marca;
    this.modelo = modelo;
  }

  // Método del objeto
  arrancar() {
    console.log(`El coche ${this.marca} ${this.modelo} está arrancando`);
  }

  // Método especial
  toString() {
    return `Coche: ${this.marca} ${this.modelo}`;
  }
}
// Crear objeto Coche
const coche1 = new Coche("Toyota", "Corolla");

// Uso del objeto
coche1.arrancar();
console.log(coche1.toString());

/* =============================================
   EJERCICIO PROPUESTO 2
   Clase Persona + Clase Profesor (herencia)
   ============================================= */
// Clase base Persona (definida dentro del ejercicio 2)
class Persona {
  #dni; // campo privado

  constructor(nombre, edad, dni) {
    this.nombre = nombre;
    this.edad = edad;
    this.#dni = dni;
  }

  // Getter y Setter
  get edad() {
    return this._edad;
  }
  set edad(valor) {
    if (valor < 0) {
      throw new Error("La edad no puede ser negativa");
    }
    this._edad = valor;
  }
  get dni() {
    return this.#dni;
  }

  // Método del objeto
  saludar() {
    console.log(`Hola, soy ${this.nombre} y tengo ${this.edad} años`);
  }

  // Método especial
  toString() {
    return `Persona: ${this.nombre}, Edad: ${this.edad}`;
  }

  // Método estático
  static esMayorDeEdad(edad) {
    return edad >= 18;
  }
}

// Clase Profesor que hereda de Persona
class Profesor extends Persona {
  constructor(nombre, edad, dni, asignatura) {
    super(nombre, edad, dni);
    this.asignatura = asignatura;
  }

  // Método propio de la subclase
  enseñar() {
    console.log(`${this.nombre} está enseñando ${this.asignatura}`);
  }

  // Sobrescritura de método
  saludar() {
    console.log(
      `Hola, soy ${this.nombre}, profesor de ${this.asignatura}`
    );
  }
}

// Crear objeto Profesor
const profesor1 = new Profesor(
  "Luis",45,"22222222D","Desarrollo Web"
);

// Uso de métodos
profesor1.saludar();
profesor1.enseñar();
console.log(profesor1.toString());
console.log("¿Es mayor de edad?", Persona.esMayorDeEdad(profesor1.edad));

// Comprobación de herencia
console.log(profesor1 instanceof Profesor); // true
console.log(profesor1 instanceof Persona);  // true