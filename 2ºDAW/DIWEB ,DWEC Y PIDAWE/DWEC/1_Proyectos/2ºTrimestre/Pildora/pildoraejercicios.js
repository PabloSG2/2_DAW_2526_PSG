//EJEMPLO 1: PERSONA 
class Persona {
  constructor(nombre, apellidos, edad, hobbies) {
    this.nombre = nombre;
    this.apellidos = apellidos;
    this.edad = edad;
    this.hobbies = hobbies;
  }
  mostrarDatos() {
    console.log(`Nombre: ${this.nombre} ${this.apellidos}`);
    console.log(`Edad: ${this.edad}`);
    console.log(`Hobbies: ${this.hobbies.join(", ")}`);
  }
}
const persona1 = new Persona("Carlos", "García López", 28, ["leer", "correr", "viajar"]);
persona1.mostrarDatos();

//EJEMPLO 2: LENGUAJES DE PROGRAMACIÓN
class LenguajesProgramacion {
  constructor(nombre, lenguajes) {
    this.nombre = nombre;
    this.lenguajes = lenguajes;
  }
  mostrarLenguajes() {
    console.log(`${this.nombre} conoce los siguientes lenguajes:`);
    for (const lenguaje of this.lenguajes) {
      console.log("- " + lenguaje);
    }
  }
  cantidadLenguajes() {
    console.log(`Total de lenguajes: ${this.lenguajes.length}`);
  }
}

const programador = new LenguajesProgramacion("Lucía", ["JavaScript", "Python", "C++", "Java"]);
programador.mostrarLenguajes();
programador.cantidadLenguajes();

//EJEMPLO A REALIZAR 1: SEMANA SANTA SEVILLA
class SemanaSanta {
  constructor(hermandad, banda, ciudad) {
    this.hermandad = hermandad;
    this.banda = banda;
    this.ciudad = ciudad;
  }

  mostrarInfo() {
    console.log(`Hermandad: ${this.hermandad}`);
    console.log(`Banda: ${this.banda}`);
    console.log(`Ciudad: ${this.ciudad}`);
  }
}

const paso = new SemanaSanta("Hermandad de la Macarena", "Banda de Cornetas y Tambores", "Sevilla");
paso.mostrarInfo();

//EJEMPLO A REALIZAR 2: FUTBOL
class Futbolista {
  constructor(nombre, equipo, posicion, anios) {
    this.nombre = nombre;
    this.equipo = equipo;
    this.posicion = posicion;
    this.anios = anios;
  }
  mostrarInfo() {
    console.log(`${this.nombre} juega en ${this.equipo} como ${this.posicion} desde hace ${this.anios} años`);
  }
}
const jugador1 = new Futbolista("Pedro", "Real Betis", "Defensa", 5);
const jugador2 = new Futbolista("Juan", "Sevilla FC", "Delantero", 3);
jugador1.mostrarInfo();
jugador2.mostrarInfo();