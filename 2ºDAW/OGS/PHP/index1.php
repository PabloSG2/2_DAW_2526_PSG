<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sistema de Biblioteca - POO</title>
<style>
body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background: #f4f4f4; }
h1 { text-align: center; color: #333; }
.seccion {background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
h2 { color: #007bff; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
</style>
</head>
<body>
<h1>Sistema de Biblioteca - POO en PHP</h1>
<?php

// IMPORTANTE: Incluir la clase Libro
require_once 'Libro.php';
echo "<div class='seccion'>";
echo "<h2>1. Crear Objetos (Instancias de la clase)</h2>"; // Crear el primer libro
$libro1 = new Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863); // Crear el segundo libro
$libro2 = new Libro("Cien años de soledad", "Gabriel García Márquez", 471); // Crear el tercer libro
$libro3 = new Libro("1984", "George Orwell", 326);
echo "<p> Se han creado 3 libros en la biblioteca</p>"?;
echo "</div>";
// ======================================== MOSTRAR INFORMACIÓN DE LOS LIBROS
echo "<div class='seccion'>";
echo "<h2>2. Mostrar información usando métodos</h2>";
$libro1->mostrarInfo();
$libro2->mostrarInfo();
$libro3->mostrarInfo();
echo "</div>";
// ======================================== ACCESO DIRECTO A PROPIEDADES PÚBLICAS
echo "<div class='seccion'>";
echo "<h2>3. Acceso directo a propiedades públicas</h2>";
echo "<p>Título del libro 1: <strong>{$libro1->titulo}</strong></p>";
echo "<p>Autor del libro 2: <strong>{$libro2->autor}</strong></p>";
echo "<p>Páginas del libro 3: <strong>{$libro3->numeroPaginas}</strong></p>";
// También podemos MODIFICAR propiedades directamente
echo "<hr>";
echo "<p>?? Cambiando el número de páginas del libro 1...</p>";
$libro1->numeroPaginas = 900;
echo "<p>Nuevo número de páginas: <strong>{$libro1->numeroPaginas}</strong></p>";
echo "</div>";
// ======================================== USAR MÉTODOS PARA CAMBIAR ESTADO
echo "<div class='seccion'>";
echo "<h2>4. Usar métodos para realizar acciones</h2>"; // Prestar libros
$libro1->prestar();
$libro2->prestar();
echo "<hr>"; // Intentar prestar un libro ya prestado
echo "<p><strong>Intentando prestar el libro 1 otra vez:</strong></p>";
$libro1->prestar();
echo "<hr>"; // Devolver libros
echo "<p><strong>Devolviendo libros:</strong></p>";
$libro1->devolver();
echo "</div>";
// ======================================== ESTADO FINAL DE LOS LIBROS
echo "<div class='seccion'>";
echo "<h2>5. Estado final de todos los libros</h2>";
$libro1->mostrarInfo();
$libro2->mostrarInfo();
$libro3->mostrarInfo();
echo "</div>";
?>
</body>
</html>