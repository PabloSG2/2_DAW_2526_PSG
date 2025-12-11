cto->nombre = $_POST['nombre'] ?? '';
 $this->producto->descripcion = $_POST['descripcion'] ?? '';
 $this->producto->precio = $_POST['precio'] ?? 0;
 $this->producto->stock = $_POST['stock'] ?? 0;
 if ($this->producto->crear()) {
 header("Location: index.php?mensaje=producto_creado");
 exit();
 } else {
 $error = "Error al crear el producto";
 require_once 'views/productos/crear.php';
 }
 }
 }
 /**
 * Muestra los detalles de un producto
 */
 public function detalle() {
 $this->producto->id = $_GET['id'] ?? 0;
 $this->producto->obtenerPorId();

 require_once 'views/productos/detalle.php';
 }
 /**
 * Elimina un producto
 */
 public function eliminar() {
 if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 $this->producto->id = $_POST['id'] ?? 0;

 if ($this->producto->eliminar()) {
 header("Location: index.php?mensaje=producto_eliminado");
 exit();
 }
 }
 }
}
?>