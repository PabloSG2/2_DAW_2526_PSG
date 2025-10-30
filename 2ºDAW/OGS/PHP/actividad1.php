<?php
echo "Servidor ".$_SERVER['SERVER_SOFTWARE']. "<br>";
echo "Direccion IP Server: ".$_SERVER['SERVER_ADDR']. "<br>";
echo "Puerto ".$_SERVER['REMOTE_PORT']. "<br>";
echo "Direccion IP Cliente: ".$_SERVER['REMOTE_ADDR']. "<br>";
echo "Agente Cliente: ".$_SERVER['HTTP_USER_AGENT']. "<br>";
echo "Método de consulta: ".$_SERVER['REQUEST_METHOD']. "<br>";
echo "Funciones php día y hora" .date('l jS \of F Y h:i:s A');
?>