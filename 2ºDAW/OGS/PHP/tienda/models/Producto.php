<?php
class Producto {
 private $conn;
 private $table_name = "productos";
 // Propiedades del producto
 public $id;
 public $nombre;
 public $descripcion;
 public $precio;
 public $stock;
 public $fecha_creacion;
 /**
 * Constructor: recibe la conexión a la base de datos
 */
 public function __construct($db) {
 $this->conn = $db;
 }
 /**
 * Obtener todos los productos
 * @return PDOStatement
 */
 public function obtenerTodos() {
 $query = "SELECT * FROM " . $this->table_name . " ORDER BY id DESC";
 $stmt = $this->conn->prepare($query);
 $stmt->execute();
 return $stmt;
 }
 /**
 * Obtener un producto por ID
 * @return void
 */
 public function obtenerPorId() {
 $query = "SELECT * FROM " . $this->table_name . " WHERE id = :id LIMIT 1";
 $stmt = $this->conn->prepare($query);
 $stmt->bindParam(":id", $this->id);
 $stmt->execute();
 $row = $stmt->fetch();
 if ($row) {
 $this->nombre = $row['nombre'];
 $this->descripcion = $row['descripcion'];
 $this->precio = $row['precio'];
 $this->stock = $row['stock'];
 $this->fecha_creacion = $row['fecha_creacion'];
 }
 }
/**
 * Crear un nuevo producto
 * @return bool
 */
 public function crear() {
 $query = "INSERT INTO " . $this->table_name . "
 (nombre, descripcion, precio, stock)
 VALUES (:nombre, :descripcion, :precio, :stock)";
 $stmt = $this->conn->prepare($query);
 // Limpiar datos
 $this->nombre = htmlspecialchars(strip_tags($this->nombre));
 $this->descripcion = htmlspecialchars(strip_tags($this->descripcion));
 $this->precio = htmlspecialchars(strip_tags($this->precio));
 $this->stock = htmlspecialchars(strip_tags($this->stock));
 // Vincular parámetros
 $stmt->bindParam(":nombre", $this->nombre);
 $stmt->bindParam(":descripcion", $this->descripcion);
 $stmt->bindParam(":precio", $this->precio);
 $stmt->bindParam(":stock", $this->stock);
 if ($stmt->execute()) {
 return true;
 }
 return false;
 }
 /**
 * Eliminar un producto
 * @return bool
 */
 public function eliminar() {
 $query = "DELETE FROM " . $this->table_name . " WHERE id = :id";
 $stmt = $this->conn->prepare($query);

 $this->id = htmlspecialchars(strip_tags($this->id));
 $stmt->bindParam(":id", $this->id);
 if ($stmt->execute()) {
 return true;
 }
 return false;
 }
}
?>