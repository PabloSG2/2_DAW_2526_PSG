// Pedir nombre al usuario
let nombre = prompt("Introduce tu nombre:");

// Confirmar si quiere salir
let salir = confirm("¿Quieres abandonar el programa?");

// Alertar decisión
if (salir) {
  alert(nombre + ", has decidido abandonar el programa.");
} else {
  alert(nombre + ", has decidido continuar.");
}

// Mostrar mensaje en consola (color azul, negrita y subrayado)
console.log("%cFIN DEL PROGRAMA", "color: blue; font-weight: bold; text-decoration: underline;");
