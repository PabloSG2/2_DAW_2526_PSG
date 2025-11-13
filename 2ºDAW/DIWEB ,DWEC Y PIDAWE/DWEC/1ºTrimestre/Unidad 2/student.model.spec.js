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

// 2. Mostrar en consola el nombre inicial del alumno.

// 3. Actualizar el nombre del alumno para añadir un segundo apellido.

// 4. Mostrar el nombre actualizado.

// 5. Mostrar el ID único del alumno.

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

// 2.2. Convertir el timestamp (que es un 'string') a un 'number'.

// 2.3. Crear un nuevo objeto `Date` (const creationDate) usando el timestamp numérico.

// 2.4. Mostrar la fecha de creación en consola en un formato localizado (ej. 'es-ES').

// 2.5. Obtener y mostrar por separado:
//    - El año de creación (getFullYear).
//    - El mes de creación (getMonth - ¡Cuidado! Es base 0).
//    - El día de la semana (getDay - ¡Cuidado! Es base 0).

// 2.6. (Simulacro BBDD) Formatear la fecha 'creationDate' manualmente al
//    formato ISO 'YYYY-MM-DD'. (Ej: "2025-11-20").
//    Mostrar este string en consola.

// 2.7. (Cálculo) Crear una nueva fecha (const futureDate) y usar `setMonth()`
//    para establecerla 6 meses en el futuro respecto a 'creationDate'.
//    Mostrar la nueva fecha.

// 2.8. (Cálculo) Calcular cuántos milisegundos han pasado desde que se creó
//    el alumno (creationDate.getTime()) hasta ahora (Date.now()).
//    Convertir ese total a segundos y mostrarlo.

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

// 3.2. Mostrar en consola el número de asignaturas que tiene el alumno.

// 3.3. Comprobar si el alumno tiene nota en "Programación" y mostrar el resultado.

// 3.4. Eliminar una de las asignaturas añadidas usando `_grades.delete()`.

// 3.5. Comprobar que la asignatura ha sido borrada (usando .hasGrade()) y
//    mostrar el nuevo tamaño del Map.

// 3.6. Iterar sobre el Map de notas (`_grades`) usando `.forEach()` e
//    imprimir cada asignatura y su nota.

// 3.7. Obtener un array solo con las CLAVES (asignaturas) del Map.

// 3.8. Obtener un array solo con los VALORES (notas) del Map.

// 3.9. Eliminar TODAS las notas del alumno de golpe.

// 3.10. Mostrar el tamaño final del Map (debería ser 0).

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

// 4.1. Obtener la lista de notas (const gradesList) usando `getGradesList()`.
//    Mostrarla en consola (usar `console.table` para mejor visualización).

// 4.2. (Array.map) Crear un NUEVO array que contenga solo los NOMBRES
//    de las asignaturas. Mostrar el nuevo array en consola.

// 4.3. (Array.filter) Crear un NUEVO array que contenga solo los
//    objetos de las asignaturas APROBADAS (nota >= 5). Mostrar en consola.

// 4.4. (Array.find) Encontrar el objeto de la asignatura
//    "Bases de datos" y mostrarlo en consola.

// 4.5. (Array.reduce) Usar `.reduce()` sobre la lista de notas para
//    calcular la suma total de todas las notas. Mostrar la suma.

// 4.6. (Array.some) Comprobar si el alumno tiene "alguna"
//    asignatura suspensa (nota < 5). Mostrar true/false.

// 4.7. (Array.every) Comprobar si "todas" las asignaturas
//    del alumno están aprobadas (nota >= 5). Mostrar true/false.

// 4.8. (Array.sort) Crear un NUEVO array que sea una copia de
//    `gradesList` y ordenarlo por nota (score) de menor a mayor.
//    Mostrar el array ordenado.

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

// 5.2. Obtener la referencia al elemento `<ul id="student-list">` del DOM.
//    (Si da error, asegurarse de haber añadido el <ul> al HTML).

// 5.3. Iterar sobre la lista de nombres (Array del paso 1).
//    Dentro del bucle:
//    A. Crear un nuevo elemento `<li>`.
//    B. Asignar el nombre del alumno al `textContent` del `<li>`.
//    C. Añadir el `<li>` como hijo del `<ul>`.

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
// const gradesList = student1.getGradesList();

// 6.1. Mostrar en consola el TIPO de dato de:
//    - student1
//    - student1.getName()
//    - student1.getAverage()
//    - student1._grades
//    - gradesList

// 6.2. Comprobar si `student1` es una instancia de `Student`. Mostrar true/false.

// 6.3. Comprobar si `student1._grades` es una instancia de `Map`. Mostrar true/false.

// 6.4. Comprobar si `gradesList` es una instancia de `Array`. Mostrar true/false.

// 6.5. Obtener un array con los nombres de las propiedades INTERNAS
//    (ej: "_id", "_name") del objeto `student1`.

// 6.6. Comprobar si `student1` tiene "directamente" la propiedad `_name`.

// 6.7. Comprobar si `student1` tiene la propiedad `toString`.
//    (¿Por qué da `false` si `student1.toString()` funciona? Investigar).

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