<?php
require_once 'controllers/ProductoController.php';
// Crear instancia del controlador
$controller = new ProductoController();
// Obtener la acción solicitada (por defecto: index)
$accion = $_GET['accion'] ?? 'index';
// Ejecutar la acción correspondiente
switch ($accion) {
 case 'index':
 $controller->index();
 break;

 case 'crear':
 $controller->crear();
 break;

 case 'guardar':
 $controller->guardar();
 break;

 case 'detalle':
 $controller->detalle();
 break;

 case 'eliminar':
 $controller->eliminar();
 break;

 default:
 $controller->index();
 break;
}
?>