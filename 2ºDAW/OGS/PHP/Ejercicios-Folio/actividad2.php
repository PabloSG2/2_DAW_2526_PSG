<?php
$nombre= 'Pablo'; $apellido= "SG";
$edad= 20; $año= "27-2-2025";
$peso= 85;  $altura = 185; 
$coche= false; $telefono = null;
$lenguajes  = array (
    0 => "PHP" , 
    1 => "MYSQL", 
    2 => "JavaScript",
    3 => "Phython"
);
define("NOM_SITIO", "Pablo");
define("VER_SITIO", "Pablo1");

echo "<b>Nombre:</b> $nombre <br>";
echo '<b>Nombre:</b>  $nombre <br>';
echo "<b>Nombre:</b>" .$nombre. "<br>";
echo "gettype($peso) <br>";
echo "<b>Doble de la edad:</b> ".$edad*2; echo "<br>";
printf("%.2f cm", $altura);
if ($coche == true) {
    echo "<br>Tiene coche<br>";
}else {
    echo "<br>No tiene coche<br>";
}
print_r($lenguajes); echo "<br>";
foreach($lenguajes as $lenguaje) {
    echo "<b>Lenguaje:</b> " .$lenguaje. "<br>";
}
echo "<b><br>IMC Calculado:</b> " .$peso/($altura*$altura);
echo "<b><br>NombreSitio:</b> ".NOM_SITIO;
echo "<b><br>VerSitio:</b> " .VER_SITIO;
?>