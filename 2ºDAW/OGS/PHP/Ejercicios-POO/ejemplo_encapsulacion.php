<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Encapsulación en POO</title>
<style>
body { font-family: Arial, sans-serif; max-width: 900px; margin: 50px auto; padding: 20px; background: #f4f4f4; }
h1 { text-align: center; color: #333; }
.seccion {background: white; padding: 20px; margin: 20px 0; border-radius: 10px; ox-shadow: 0 2px 5px rgba(0,0,0,0.1);}
h2 { color: #28a745; border-bottom: 2px solid #28a745; padding-bottom: 10px; }
.codigo { background: #f5f5f5; padding: 10px; border-left: 4px solid #28a745; font-family: monospace; margin: 10px 0; }
</style>
</head>
<body>
<h1>Encapsulación y Getters/Setters</h1>
<?php
require_once 'LibroMejorado.php';
echo "<div class='seccion'>";
echo "<h2>1. Crear libro con propiedades privadas</h2>";
$libro = new LibroMejorado( "El Principito", "Antoine de Saint-Exupéry", 96, "978-0156012195" );
echo "<p> Libro creado correctamente</p>"?;
$libro->mostrarInfo();
echo "</div>";
// ======================================== INTENTAR ACCESO DIRECTO (NO FUNCIONARÁ)
echo "<div class='seccion'>";
echo "<h2>2. Diferencia entre propiedades públicas y privadas</h2>";
echo "<p><strong> Si intentamos acceder directamente a una propiedad privada:</strong></p>"?;
echo "<div class='codigo'>";
echo "// echo \$libro->titulo; <-- Esto daría ERROR<br>";
echo "// PHP Fatal error: Cannot access private property";
echo "</div>";
echo "<p><strong> Debemos usar los métodos GETTER:</strong></p>"?;
echo "<div class='codigo'>";
echo "echo \$libro->getTitulo(); <-- Esto funciona correctamente";
echo "</div>";
echo "<p>Título del libro: <strong>" . $libro->getTitulo() . "</strong></p>";
echo "<p>Autor del libro: <strong>" . $libro->getAutor() . "</strong></p>";
echo "<p>ISBN: <strong>" . $libro->getIsbn() . "</strong></p>";
echo "</div>";
// ======================================== USAR SETTERS CON VALIDACIÓN
echo "<div class='seccion'>";
echo "<h2>3. Modificar propiedades usando SETTERS (con validación)</h2>";
echo "<p><strong>Intentando cambiar el título a algo válido:</strong></p>";
$libro->setTitulo("El Principito - Edición Ilustrada");
echo "<p>Nuevo título: <strong>" . $libro->getTitulo() . "</strong></p>";
echo "<hr>";
echo "<p><strong>Intentando cambiar el título a algo inválido (menos de 3 caracteres):</strong></p>";
$libro->setTitulo("El");
echo "<hr>";
echo "<p><strong>Intentando cambiar el número de páginas a un valor negativo:</strong></p>";
$libro->setNumeroPaginas(-50);
echo "<hr>";
echo "<p><strong>Cambiando el número de páginas a un valor válido:</strong></p>";
$libro->setNumeroPaginas(120);
echo "<p>Nuevo número de páginas: <strong>" . $libro->getNumeroPaginas() . "</strong></p>";
echo "</div>";
// ======================================== USAR MÉTODOS ADICIONALES
echo "<div class='seccion'>";
echo "<h2>4. Métodos adicionales de la clase</h2>";
echo "<p> Tiempo de lectura estimado: <strong>"?? . $libro->tiempoLecturaEstimado() . "</strong></p>";
echo "</div>";
// ======================================== ESTADO FINAL
echo "<div class='seccion'>";
echo "<h2>5. Estado final del libro</h2>";
$libro->mostrarInfo();
echo "</div>";
?>
<div class="seccion">
<h2>¿Por qué usar PRIVATE y getters/setters?</h2>
<ul>
<li><strong>Control:</strong> Podemos validar los datos antes de modificarlos</li>
<li><strong>Seguridad:</strong> Evitamos que se modifiquen datos de forma incorrecta</li>
<li><strong>Flexibilidad:</strong> Podemos cambiar cómo funcionan internamente sin afectar el código externo</li>
<li><strong>Mantenimiento:</strong> Es más fácil encontrar errores y hacer cambios</li>
</ul>
</div>
</body>
</html>
