// archivo: js/model/student.model.spec.js
// --- TALLER PRÁCTICO: OBJETOS, COLECCIONES Y DOM ---
//
// * Objetivo: Usar la clase Student como base para practicar
// * conceptos fundamentales de JavaScript (Mapas, Fechas, Arrays, DOM, Tipos).
// *
// * Uso: Incluir este archivo en index.html DESPUÉS de student.model.js.
// *
// * Ejecución: Abrir la consola del navegador (F12 > Console) para ver los
// * resultados y completar los ejercicios.
// *
// * @see [student.model.js](student.model.js)
// * @see [Cheatsheet JS](javascript-cheatsheet-2019.pdf)
// * @see [MDN - Referencia de JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference)

console.log("--- Taller Práctico de student.model.spec.js (F12) ---");

// ========================================================================
// SECCIÓN 1: CALENTAMIENTO (Creación y Métodos)
// ========================================================================
console.groupCollapsed("TALLER 1: Creación de instancias");

/**
 * @purpose Demostrar la creación de objetos (instancias) y el uso de métodos
 * (getters/setters) de la clase Student.
 */

// --- ZONA DE TRABAJO 1 ---
// 1. Crear un nuevo alumno (const student1) con un nombre y curso "1".
const student1 = new Student("Juan Pérez", "1"); // Creamos instancia de Student

// 2. Mostrar en consola el nombre inicial del alumno.
console.log("Nombre inicial:", student1.getName()); // Mostramos el nombre

// 3. Actualizar el nombre del alumno para añadir un segundo apellido.
student1.setName("Juan Pérez García"); // Actualizamos nombre con segundo apellido

// 4. Mostrar el nombre actualizado.
console.log("Nombre actualizado:", student1.getName()); // Mostramos el nuevo nombre

// 5. Mostrar el ID único del alumno.
console.log("ID del alumno:", student1.getId()); // Mostramos ID generado

console.groupEnd();


// ========================================================================
// SECCIÓN 2: EXPLORANDO EL OBJETO 'Date' (Usando el ID)
// ========================================================================
console.groupCollapsed("TALLER 2: Explorando 'Date' (Fechas)");

/**
 * @purpose Practicar el manejo de Fechas (Date), cálculos y formateo.
 * @context El ID del alumno (`this._id`) se genera usando `Date.now()`.
 * Se debe manipular este timestamp.
 * @see [MDN - Objeto Date](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Date)
 * @see [Cheatsheet: Date Methods](javascript-cheatsheet-2019.pdf)
 */

// --- ZONA DE TRABAJO 2 ---
// (Usar el 'student1' creado en el Taller 1)

// 2.1. Extraer el timestamp (el número) del ID del 'student1'.
const timestampString = student1.getId(); // Obtenemos ID (timestamp como string)
console.log("Timestamp string:", timestampString);

// 2.2. Convertir el timestamp (que es un 'string') a un 'number'.
const timestampNumber = Number(timestampString); // Convertimos string a number
console.log("Timestamp number:", timestampNumber);

// 2.3. Crear un nuevo objeto `Date` (const creationDate) usando el timestamp numérico.
const creationDate = new Date(timestampNumber); // Creamos Date a partir del timestamp

// 2.4. Mostrar la fecha de creación en consola en un formato localizado (ej. 'es-ES').
console.log("Fecha creación (ES):", creationDate.toLocaleString("es-ES"));

// 2.5. Obtener y mostrar por separado:
//    - El año de creación (getFullYear).
//    - El mes de creación (getMonth - ¡Cuidado! Es base 0).
//    - El día de la semana (getDay - ¡Cuidado! Es base 0).
console.log("Año:", creationDate.getFullYear()); // Año completo
console.log("Mes (0-11):", creationDate.getMonth()); // Mes (base 0)
console.log("Día semana (0-Domingo):", creationDate.getDay()); // Día de la semana

// 2.6. (Simulacro BBDD) Formatear la fecha 'creationDate' manualmente al
//    formato ISO 'YYYY-MM-DD'. (Ej: "2025-11-20").
//    Mostrar este string en consola.
const isoFormat =
  creationDate.getFullYear() +
  "-" +
  String(creationDate.getMonth() + 1).padStart(2, "0") +
  "-" +
  String(creationDate.getDate()).padStart(2, "0");
console.log("Fecha en ISO manual:", isoFormat);

// 2.7. (Cálculo) Crear una nueva fecha (const futureDate) y usar `setMonth()`
//    para establecerla 6 meses en el futuro respecto a 'creationDate'.
//    Mostrar la nueva fecha.
const futureDate = new Date(creationDate);
futureDate.setMonth(futureDate.getMonth() + 6); // Sumamos 6 meses
console.log("Fecha + 6 meses:", futureDate.toLocaleString("es-ES"));

// 2.8. (Cálculo) Calcular cuántos milisegundos han pasado desde que se creó
//    el alumno (creationDate.getTime()) hasta ahora (Date.now()).
//    Convertir ese total a segundos y mostrarlo.
const diffMs = Date.now() - creationDate.getTime(); // Diferencia en ms
console.log("Segundos desde creación:", diffMs / 1000); // Convertimos a segundos

console.groupEnd();


// ========================================================================
// SECCIÓN 3: EXPLORANDO EL OBJETO 'Map' (Notas)
// ========================================================================
console.groupCollapsed("TALLER 3: Explorando 'Map' (Colección de Notas)");

/**
 * @purpose Practicar el uso avanzado de la estructura de datos Map
 * (añadir, borrar, iterar).
 * @context La clase Student usa un Map (`this._grades`) para guardar las notas.
 * @see [MDN - Objeto Map](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map)
 * @see [Cheatsheet: Map Methods](javascript-cheatsheet-2019.pdf)
 */

// --- ZONA DE TRABAJO 3 ---
// (Seguir usando el 'student1' del Taller 1)

// 3.1. Añadir 4 asignaturas (a elección) con notas al 'student1'.
student1.setOrAddGrade("Programación", 8);
student1.setOrAddGrade("Bases de datos", 6);
student1.setOrAddGrade("Entornos", 7);
student1.setOrAddGrade("Sistemas", 5);

// 3.2. Mostrar en consola el número de asignaturas que tiene el alumno.
console.log("Número de asignaturas:", student1._grades.size);

// 3.3. Comprobar si el alumno tiene nota en "Programación" y mostrar el resultado.
console.log("¿Tiene Programación?:", student1.hasGrade("Programación"));

// 3.4. Eliminar una de las asignaturas añadidas usando `_grades.delete()`.
student1._grades.delete("Entornos");

// 3.5. Comprobar que la asignatura ha sido borrada (usando .hasGrade()) y
//    mostrar el nuevo tamaño del Map.
console.log("¿Entornos existe?:", student1.hasGrade("Entornos"));
console.log("Nuevo tamaño:", student1._grades.size);

// 3.6. Iterar sobre el Map de notas (`_grades`) usando `.forEach()` e
//    imprimir cada asignatura y su nota.
student1._grades.forEach((nota, asignatura) => {
  console.log(asignatura, ":", nota);
});

// 3.7. Obtener un array solo con las CLAVES (asignaturas) del Map.
const keys = [...student1._grades.keys()];
console.log("Claves:", keys);

// 3.8. Obtener un array solo con los VALORES (notas) del Map.
const values = [...student1._grades.values()];
console.log("Valores:", values);

// 3.9. Eliminar TODAS las notas del alumno de golpe.
student1._grades.clear();

// 3.10. Mostrar el tamaño final del Map (debería ser 0).
console.log("Tamaño final (0):", student1._grades.size);

console.groupEnd();


// ========================================================================
// SECCIÓN 4: EXPLORANDO MÉTODOS DE 'Array'
// ========================================================================
console.groupCollapsed("TALLER 4: Explorando Métodos de 'Array'");

/**
 * @purpose Practicar los métodos de transformación e iteración de Arrays.
 * @context El método .getGradesList() nos devuelve un Array de objetos.
 * @see [MDN - Objeto Array](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array)
 * @see [Cheatsheet: Array Methods](javascript-cheatsheet-2019.pdf)
 */

// --- ZONA DE TRABAJO 4 ---
// (Volver a añadir 3-4 notas al 'student1' para este taller)
// ...
student1.setOrAddGrade("Programación", 8);
student1.setOrAddGrade("BD", 4);
student1.setOrAddGrade("Sistemas", 6);
student1.setOrAddGrade("Marcas", 9);

// 4.1. Obtener la lista de notas (const gradesList) usando `getGradesList()`.
//    Mostrarla en consola (usar `console.table` para mejor visualización).
const gradesList = student1.getGradesList();
console.table(gradesList); // Visualización en tabla

// 4.2. (Array.map) Crear un NUEVO array que contenga solo los NOMBRES
//    de las asignaturas. Mostrar el nuevo array en consola.
const nombres = gradesList.map(g => g.subject);
console.log("Nombres:", nombres);

// 4.3. (Array.filter) Crear un NUEVO array que contenga solo los
//    objetos de las asignaturas APROBADAS (nota >= 5). Mostrar en consola.
const aprobadas = gradesList.filter(g => g.score >= 5);
console.log("Aprobadas:", aprobadas);

// 4.4. (Array.find) Encontrar el objeto de la asignatura
//    "Bases de datos" y mostrarlo en consola.
const bd = gradesList.find(g => g.subject === "Bases de datos" || g.subject === "BD");
console.log("Encontrado BD:", bd);

// 4.5. (Array.reduce) Usar `.reduce()` sobre la lista de notas para
//    calcular la suma total de todas las notas. Mostrar la suma.
const suma = gradesList.reduce((acc, g) => acc + g.score, 0);
console.log("Suma notas:", suma);

// 4.6. (Array.some) Comprobar si el alumno tiene "alguna"
//    asignatura suspensa (nota < 5). Mostrar true/false.
console.log("¿Alguna suspensa?:", gradesList.some(g => g.score < 5));

// 4.7. (Array.every) Comprobar si "todas" las asignaturas
//    del alumno están aprobadas (nota >= 5). Mostrar true/false.
console.log("¿Todas aprobadas?:", gradesList.every(g => g.score >= 5));

// 4.8. (Array.sort) Crear un NUEVO array que sea una copia de
//    `gradesList` y ordenarlo por nota (score) de menor a mayor.
//    Mostrar el array ordenado.
const sorted = [...gradesList].sort((a, b) => a.score - b.score);
console.log("Ordenado:", sorted);

console.groupEnd();

// ========================================================================
// SECCIÓN 5: MANIPULACIÓN DEL DOM (Dibujando datos)
// ========================================================================
console.groupCollapsed("TALLER 5: Manipulación del DOM");

/**
 * @purpose Practicar cómo "pintar" datos de JS en el HTML.
 * @context Usar la lista estática STUDENTS_BY_COURSE_MAP
 * para dibujar una lista de alumnos en el index.html.
 * @note PARA ESTE EJERCICIO: Añadir un <ul> vacío con id="student-list"
 * en el archivo index.html (ej. debajo de la tabla).
 * @see [Cheatsheet: DOM Methods](javascript-cheatsheet-2019.pdf)
 */

// --- ZONA DE TRABAJO 5 ---
// 5.1. Obtener la lista de alumnos de 1º DAW (Array)
//    desde `STUDENTS_BY_COURSE_MAP`.
const lista1DAW = STUDENTS_BY_COURSE_MAP.get("1");

// 5.2. Obtener la referencia al elemento `<ul id="student-list">` del DOM.
//    (Si da error, asegurarse de haber añadido el <ul> al HTML).
const ul = document.getElementById("student-list");

// 5.3. Iterar sobre la lista de nombres (Array del paso 1).
//    Dentro del bucle:
//    A. Crear un nuevo elemento `<li>`.
//    B. Asignar el nombre del alumno al `textContent` del `<li>`.
//    C. Añadir el `<li>` como hijo del `<ul>`.
lista1DAW.forEach(nombre => {
  const li = document.createElement("li"); // Crear <li>
  li.textContent = nombre; // Asignar nombre
  ul.appendChild(li); // Añadir al <ul>
});

console.groupEnd();


// ========================================================================
// SECCIÓN 6: INSPECCIÓN DE OBJETOS Y TIPOS
// ========================================================================
console.groupCollapsed("TALLER 6: Inspección de Objetos y Tipos");

/**
 * @purpose Practicar la introspección de objetos y la comprobación de tipos.
 * @see [MDN - typeof](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/typeof)
 * @see [MDN - instanceof](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/instanceof)
 * @see [MDN - Object.keys](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Object/keys)
 * @see [MDN - hasOwnProperty](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty)
 */

// --- ZONA DE TRABAJO 6 ---
// (Usar el 'student1' y `gradesList` de talleres anteriores)
const gradesList2 = student1.getGradesList();

// 6.1. Mostrar en consola el TIPO de dato de:
//    - student1
//    - student1.getName()
//    - student1.getAverage()
//    - student1._grades
//    - gradesList
console.log(typeof student1);
console.log(typeof student1.getName());
console.log(typeof student1.getAverage());
console.log(typeof student1._grades);
console.log(typeof gradesList2);

// 6.2. Comprobar si `student1` es una instancia de `Student`. Mostrar true/false.
console.log(student1 instanceof Student);

// 6.3. Comprobar si `student1._grades` es una instancia de `Map`. Mostrar true/false.
console.log(student1._grades instanceof Map)

// 6.4. Comprobar si `gradesList` es una instancia de `Array`. Mostrar true/false.
console.log(gradesList2 instanceof Array);

// 6.5. Obtener un array con los nombres de las propiedades INTERNAS
//    (ej: "_id", "_name") del objeto `student1`.
console.log(Object.keys(student1));

// 6.6. Comprobar si `student1` tiene "directamente" la propiedad `_name`.
console.log(student1.hasOwnProperty("_name"));

// 6.7. Comprobar si `student1` tiene la propiedad `toString`.
//    (¿Por qué da `false` si `student1.toString()` funciona? Investigar).
console.log(student1.hasOwnProperty("toString")); // false, viene del prototipo

console.groupEnd();


// ========================================================================
// SECCIÓN 7: RETOS (Ejercicios propuestos)
// ========================================================================
console.groupCollapsed("TALLER 7: Retos");

/**
 * @purpose Ejercicios de reto para afianzar y ampliar la clase Student.
 */

// --- ZONA DE TRABAJO 7 ---

/*
 * --- Reto 1: MODIFICACIÓN (en student.model.js) ---
 *
 * Modificar el método setOrAddGrade() en 'student.model.js'.
 * Añadir una validación para que solo acepte notas que sean
 * de tipo 'number' y que estén en el rango de 0 a 10.
 * Si la nota no es válida, no debe añadirse al Map.
 *
 * (No hay código que rellenar aquí, es una modificación en el otro archivo.
 * Probarlo aquí después de modificarlo).
 */


/*
 * --- Reto 2: AMPLIACIÓN (en student.model.js) ---
 *
 * Añadir un nuevo método getHighestGrade() a la clase Student.
 * Este método debe iterar por el Map 'this._grades' y devolver
 * la nota más alta (el número). Si no hay notas, debe devolver 0.
 *
 * (No hay código que rellenar aquí, es una modificación en el otro archivo.
 * Probarlo aquí después de modificarlo).
 */
// const studentConNotas = new Student("Prueba Reto 2", "1");
// studentConNotas.setOrAddGrade("Materia A", 5);
// studentConNotas.setOrAddGrade("Materia B", 9);
// studentConNotas.setOrAddGrade("Materia C", 7);
// console.log("Nota más alta (debe ser 9):", studentConNotas.getHighestGrade());


/*
 * --- Reto 3: PRÁCTICA DE ITERADORES (Map vs Array) ---
 *
 * El objetivo es demostrar la diferencia práctica entre iterar
 * un Map (`_grades`) y un Array (`gradesList`).
 */

// 3.A. (Iterar el Map)
// Usar `student1._grades.forEach(...)`.
// Imprimir en consola los argumentos (valor, clave) que recibe la función.
// Formato de salida esperado: "CLAVE: [nombre_asignatura], VALOR: [nota]"

// console.log("--- Iterando el Map (_grades) ---");
// (Asegurarse de que student1 tenga notas)
// student1._grades.forEach((value, key) => {
//   ...
// });


// 3.B. (Iterar el Array)
// Obtener `gradesList` usando `student1.getGradesList()`.
// Usar `gradesList.forEach(...)`.
// Imprimir en consola los argumentos (elemento, índice) que recibe la función.
// Formato de salida esperado: "ÍNDICE: [index], ELEMENTO: [objeto_de_nota]"

// console.log("--- Iterando el Array (gradesList) ---");
// const gradesList = student1.getGradesList();
// gradesList.forEach((element, index) => {
//   ...
// });

console.groupEnd();