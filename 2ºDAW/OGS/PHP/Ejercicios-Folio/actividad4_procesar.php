<?php
if (isset($_POST['enviar'])
    && !empty($_POST['nombre'])
    && !empty($_POST['edad'])
    && !empty($_POST['lenguajes'])) {

    // Recogemos los datos enviados por el formulario
    $nombre = $_POST['nombre'];
    $edad = $_POST['edad'];
    $lenguajes = $_POST['lenguajes'];

    // Mostramos los datos
    echo "<h2>Datos recibidos:</h2>";
    echo "Nombre: $nombre<br>";
    echo "Edad: $edad<br>";        
    echo "Lenguajes seleccionados:<br>";
    echo "<ul>";
    foreach ($lenguajes as $lang) {
        echo "<li>$lang</li>";
    }
    echo "</ul>";

} else {
    echo "Debes completar todos los campos y seleccionar al menos un lenguaje.";
}
?>
