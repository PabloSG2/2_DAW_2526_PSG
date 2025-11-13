// archivo: js/model/student.model.js
// --- MODELO: Lógica y Datos de Alumnos ---

/**
 * Clase que representa a un solo alumno.
 * Encapsula su nombre, curso y sus propias calificaciones.
 */
class Student {
    /**
     * @param {string} name - El nombre completo del alumno.
     * @param {string} courseId - El ID del curso ('1' o '2').
     * @see [Date.now() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Date/now)
     * @see [JavaScript Map - w3schools](https://www.w3schools.com/js/js_object_maps.asp)
     * @see [Map y Set - javascript.info](https://es.javascript.info/map-set)
     */
    constructor(name, courseId) {
        // Usamos '_' para marcar las propiedades como "internas"
        this._id = `student-${Date.now()}`; // ID único para el alumno
        this._name = name;
        this._courseId = courseId;
        
        // Estructura interna de alumnos por curso
        this._grades = new Map();
    }

    /**
     * Devuelve el ID único del alumno.
     * @returns {string}
     */
    getId() {
        return this._id;
    }

    /**
     * Devuelve el nombre del alumno.
     * @returns {string}
     */
    getName() {
        return this._name;
    }

    /**
     * Devuelve el ID del curso del alumno.
     * @returns {string}
     */
    getCourseId() {
        return this._courseId;
    }
    
    /**
     * Actualiza el nombre del alumno.
     * @param {string} newName - El nuevo nombre.
     * @see [String.trim() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/trim)
     * @see [String trim() - w3schools](https://www.w3schools.com/jsref/jsref_trim.asp)
     */
    setName(newName) {
        // Se valida que el nombre no sea nulo o esté vacío
        if (newName && newName.trim() !== '') {
            this._name = newName.trim();
        }
        // TODO: Faltaría una validación más robusta (ej. no permitir números).
    }

    /**
     * Actualiza el curso del alumno.
     * @param {string} newCourseId - El nuevo ID de curso ('1' o '2').
     */
    setCourseId(newCourseId) {
        // Se valida que el ID sea uno de los valores esperados ('1' o '2').
        // TODO: Si se añaden más cursos (ej. '3'), esta lógica debe actualizarse.
        if (newCourseId === '1' || newCourseId === '2') {
            this._courseId = newCourseId;
        }
    }

    /**
     * Establece (añade o actualiza) una nota para una asignatura específica.
     * @param {string} subject - Nombre de la asignatura.
     * @param {number} score - La nota.
     * @see [Map.set() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map/set)
     * @see [Map.set() - w3schools](https://www.w3schools.com/jsref/jsref_map_set.asp)
     */
    setOrAddGrade(subject, score) {
        // TODO: Falta la validación de la nota.
        // Se debería comprobar que 'score' es un número
        // y está en el rango (ej. 0-10) antes de guardarlo.
        this._grades.set(subject, score);
    }

    /**
     * Comprueba si el alumno ya tiene una nota para esa asignatura.
     * (Método de lectura, no requiere validación de entrada).
     * @param {string} subject - Nombre de la asignatura.
     * @returns {boolean}
     * @see [Map.has() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map/has)
     * @see [Map.has() - w3schools](https://www.w3schools.com/jsref/jsref_map_has.asp)
     */
    hasGrade(subject) {
        // Lee la propiedad interna _grades
        return this._grades.has(subject);
    }

    /**
     * Calcula la nota media del alumno basándose en sus calificaciones internas.
     * (Método de lectura, no requiere validación).
     * @returns {number} - La media calculada.
     * @see [Map.size - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map/size)
     * @see [Map.values() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map/values)
     * @see [Map.size - w3schools](https://www.w3schools.com/jsref/jsref_map_size.asp)
     */
    getAverage() {
        // Lee la propiedad interna _grades
        if (this._grades.size === 0) {
            return 0;
        }

        let sum = 0;
        // Iteramos sobre los valores (las notas) del Map
        for (let score of this._grades.values()) {
            sum += score;
        }
        
        return sum / this._grades.size;
    }

    /**
     * Obtiene un array de objetos de calificación del alumno.
     * Devuelve los datos puros del modelo (claves en inglés).
     * La Vista (view.js) será responsable de "traducir" esto.
     * @returns {Array<object>}
     * @see [Array.from() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/from)
     * @see [Map.entries() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map/entries)
     * @see [Array.prototype.map() - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
     * @see [Métodos de Arrays (map) - lenguajejs.com](https://lenguajejs.com/javascript/arrays/array-metodos/)
     */
    getGradesList() {
        // Devuelve datos puros del modelo (claves en inglés).
        return Array.from(this._grades.entries()).map(([subject, score]) => {
            // NOTA: La Vista (app.view.js) debe ser actualizada
            // para leer estas claves en inglés (subjectName, score, etc.)
            return {
                id: `${this._id}-${subject}`, 
                subjectName: subject,
                score: score,
                studentName: this._name,
                courseId: this._courseId
            };
        });
    }
}

// --- Listas de Nombres para la UI (VISTA) ---

const students1DAW = [
    "Álvaro Molina Cifuentes",
    "Antonio Jesús Medina Carrasco",
    "Beatriz Sánchez Villalba",
    "Claudia Moreno Espinosa",
    "Diego Javier Serrano Padilla",
    "Elena Jimena Rivas Montoya",
    "Francisco Manuel Ortega Roldán",
    "Isabel Cristina León Caballero",
    "Iván Cordero Salcedo",
    "Joaquín Esteban Vargas Tejada",
    "Lucía Beltrán Márquez",
    "María Fernanda Torres Llamas",
    "Miguel Ángel Bravo Zamora",
    "Nuria Gallardo Paredes",
    "Patricia Romero Barragán",
    "Raquel Domínguez Valverde",
    "Héctor Lozano Camacho"
];
// NOTA: "Héctor" se ha movido manualmente al final para coincidir con la lista original.
// Si usamos .sort(), iría con la 'H'. Para docencia, es mejor ordenarlo alfabéticamente.

const students2DAW = [
    "Alejandro Cordón García",
    "Alejandro González Macía",
    "Alejandro Montesinos Pozo",
    "Emilio Mariscal Sierra",
    "Fernando Rodríguez Gamarro",
    "Irene Osuna Delgado",
    "Jesús Romero Pérez",
    "Jorge Durán Muñoz",
    "José Javier García Flores",
    "José Joaquín Sánchez García",
    "José Miguel Sánchez Mariscal",
    "Juan Jesús González García",
    "Julio Javier Pascual Cruz",
    "Justo Puerto Delgado",
    "Manuel Jiménez Gutiérrez",
    "Manuel Verdón Torres",
    "Mireya González Ricón",
    "Noelia Díaz López",
    "Rubén Gordillo Bellido",
    "Sergio Perea Moreno"
];

/**
 * Estructura de datos optimizada (Map) para almacenar
 * los listados de alumnos por curso.
 * La clave es el ID del curso (string), el valor es el array de nombres ORDENADO.
 * @see [Map - MDN](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Map)
 * @see [Map - w3schools](https://www.w3schools.com/js/js_object_maps.asp)
 */
const STUDENTS_BY_COURSE_MAP = new Map([
    ['1', students1DAW],
    ['2', students2DAW]
]);