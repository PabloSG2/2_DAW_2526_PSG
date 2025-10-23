<?php
$nombre= 'Pablo';
$apellido= "SG";
$edad= 20;
$año= "27-2-2025";
$peso= 85;
$altura= "185cm";
$coche= false;
$lenguajes  = array (
    0 => "PHP" , 
    1 => "MYSQL", 
    2 => "JavaScript",
    3 => "Phython"
);
$telefono = null;
const Nom_Sitio= "";
const Ver_Sitio= "";

echo "Nombre: $nombre <br>";
echo 'Nombre: $nombre <br>';
echo "Nombre:" .$nombre. "<br>";
echo "gettype($peso) <br>";
echo "Doble de la edad: ".$edad*2; echo "<br>";
printf($altura);
if ($coche == true) {
    echo "<br>Tiene coche<br>";
}else {
    echo "<br>No tiene coche<br>";
}
print_r($lenguajes); echo "<br>";
foreach($lenguajes as $lenguaje) {
    echo "<br>Lenguaje: " .$lenguaje;
}
echo "<br>IMC Calculado: " .$peso/($altura*$altura);
?>