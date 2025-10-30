<html lang="es">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Ejercicio 2: PHP dentro de HTML</h1><hr>
    <?php
    // --- Definición de variables ---
    $nombre = 'Pablo';$apellido = "SG";
    $edad = 20; $año = "27-2-2025";
    $peso = 85;$altura = 1.85; 
    $coche = false; $telefono = null;
    $lenguajes = array("PHP", "MYSQL", "JavaScript", "Python");

    define("NOM_SITIO", "Pablo");
    define("VER_SITIO", "Pablo1");

    // --- Mostrar información ---
    echo "<b>Nombre:</b> $nombre <br>";
    echo '<b>Nombre (comillas simples):</b> $nombre <br>';
    echo "<b>Nombre (concatenado):</b> " . $nombre . "<br>";
    echo "<b>Tipo de dato: </b>" .$peso."<br>";
    echo "<b>Doble de la edad:</b> " . ($edad * 2) . "<br>";
    printf("<b>Altura:</b> ".$altura. "m");
    if ($coche == true) {
        echo "<br><em>Tiene coche</em><br>";
    } else {
        echo "<br><em>No tiene coche</em><br>";
    }

    echo "<br><strong>Lenguajes:</strong><br>";
    print_r($lenguajes);
    foreach ($lenguajes as $lenguaje) {
        echo "<br>Lenguaje: " . $lenguaje;
    }

    // Cálculo del IMC = peso / altura^2
    $imc = $peso / ($altura * $altura);
    echo "<br><strong>IMC Calculado:</strong> " . round($imc, 2) . "<br>";

    echo "<br><strong>Nombre del Sitio:</strong> " . NOM_SITIO;
    echo "<br><strong>Versión del Sitio:</strong> " . VER_SITIO;
    ?>
    <hr>
    <footer>
        <p>Generado con PHP embebido en HTML <?php date("Y") ?></p>
    </footer>
</body>
</html>
