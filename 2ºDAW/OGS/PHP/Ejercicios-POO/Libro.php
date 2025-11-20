<?php
/** Clase Libro Representa un libro de la biblioteca */
class Libro {
// PROPIEDADES (atributos del libro)
public $titulo;
public $autor;
public $numeroPaginas;
public $disponible;
/** CONSTRUCTOR Se ejecuta automáticamente al crear un nuevo objeto Libro */
public function __construct($titulo, $autor, $numeroPaginas) {
$this->titulo = $titulo;
$this->autor = $autor;
$this->numeroPaginas = $numeroPaginas;
$this->disponible = true; // Por defecto, el libro está disponible
}
/** MÉTODO: Muestra la información del libro */
public function mostrarInfo() {
$estado = $this->disponible ? "Disponible" : "Prestado";
echo "<div style='border: 2px solid #333; padding: 15px; margin: 10px 0; border-radius: 5px;'>";
echo "<h3>?? {$this->titulo}</h3>";
echo "<p><strong>Autor:</strong> {$this->autor}</p>";
echo "<p><strong>Páginas:</strong> {$this->numeroPaginas}</p>";
echo "<p><strong>Estado:</strong> {$estado}</p>";
echo "</div>";
}
/** MÉTODO: Prestar el libro */
public function prestar() {
if ($this->disponible) {
$this->disponible = false;
echo "<p style='color: green;'> El libro '?{$this->titulo}' ha sido prestado.</p>";
} else {
echo "<p style='color: red;'> El libro '?{$this->titulo}' ya está prestado.</p>";
}
}
/** MÉTODO: Devolver el libro */
public function devolver() {
if (!$this->disponible) {
$this->disponible = true;
echo "<p style='color: green;'> El libro '?{$this->titulo}' ha sido devuelto.</p>";
} else {
echo "<p style='color: orange;'> El libro '?? {$this->titulo}' ya estaba disponible.</p>";
}
}
}
?>