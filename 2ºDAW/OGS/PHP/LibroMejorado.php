<?php
/** Clase LibroMejorado Versión mejorada con encapsulación */
class LibroMejorado { // PROPIEDADES PRIVADAS (solo accesibles desde dentro de la clase)
private $titulo;
private $autor;
private $numeroPaginas;
private $disponible;
private $isbn;
/** CONSTRUCTOR */
public function __construct($titulo, $autor, $numeroPaginas, $isbn) {
$this->titulo = $titulo;
$this->autor = $autor;
$this->numeroPaginas = $numeroPaginas;
$this->isbn = $isbn;
$this->disponible = true;
}
// ========================================== GETTERS (métodos para OBTENER valores)
public function getTitulo() { return $this->titulo; }
public function getAutor() { return $this->autor; }
public function getNumeroPaginas() { return $this->numeroPaginas; }
public function getIsbn() { return $this->isbn; }
public function isDisponible() { return $this->disponible; }
// ========================================== SETTERS (métodos para MODIFICAR valores)
public function setTitulo($titulo) {
if (strlen($titulo) > 3) {
$this->titulo = $titulo;
return true;
} else {
echo "<p style='color: red;'> El título debe tener al menos 3 caracteres</p>"?;
return false;
}
}
public function setNumeroPaginas($numero) {
if ($numero > 0) {
$this->numeroPaginas = $numero;
return true;
} else {
echo "<p style='color: red;'> El número de páginas debe ser positivo</p>"?;
return false;
}
}
// ========================================== OTROS MÉTODOS
public function mostrarInfo() {
$estado = $this->disponible ? "Disponible" : "Prestado";
echo "<div style='border: 2px solid #28a745; padding: 15px; margin: 10px 0; border-radius: 5px; background: #f8f9fa;'>";
echo "<h3>?? {$this->titulo}</h3>";
echo "<p><strong>Autor:</strong> {$this->autor}</p>";
echo "<p><strong>ISBN:</strong> {$this->isbn}</p>";
echo "<p><strong>Páginas:</strong> {$this->numeroPaginas}</p>";
echo "<p><strong>Estado:</strong> <span style='color: " . ($this->disponible ? 'green' : 'red') . ";'>{$estado}</span></p>";
echo "</div>";
}
public function prestar() {
if ($this->disponible) {
$this->disponible = false;
return true;
}
return false;
}
public function devolver() {
if (!$this->disponible) {
$this->disponible = true;
return true;
}
return false;
}
/** Método para calcular tiempo de lectura estimado (basado en 1 página por minuto) */
public function tiempoLecturaEstimado() {
$horas = floor($this->numeroPaginas / 60);
$minutos = $this->numeroPaginas % 60;
return "{$horas} horas y {$minutos} minutos";
}
}
?>
