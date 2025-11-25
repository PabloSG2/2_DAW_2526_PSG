// Introducción a la POO en JavaScript
// 1. Clase Persona básica
class Persona {
    // El constructor inicializa las propiedades del objeto
    constructor(nombre, edad) {
        this.nombre = nombre; // Propiedad nombre
        this.edad = edad;     // Propiedad edad
    }
    // Método que hace que la persona salude
    saludar() {
        console.log("Hola, soy " + this.nombre);
    }
}

// 2. Subclase Estudiante que hereda de Persona
class Estudiante extends Persona {
    // Método que hace que la persona esté estudiando
    estudiar() {
        console.log(this.nombre + " está estudiando");
    }
}

// Ejemplo 1: Crear un objeto Persona y usar su método
const persona = new Persona("Carlos", 28);
persona.saludar(); // Hola, soy Carlos

// Ejemplo 2: Crear un objeto Estudiante y usar métodos heredados y propios
const estudiante1 = new Estudiante("Lucía", 18);
estudiante1.saludar();   // Hola, soy Lucía
estudiante1.estudiar();  // Lucía está estudiando