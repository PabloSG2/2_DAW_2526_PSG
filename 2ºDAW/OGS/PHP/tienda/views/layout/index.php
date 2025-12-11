<?php require_once 'views/layout/header.php'; ?>
<?php
// Mostrar mensajes
if (isset($_GET['mensaje'])) {
 if ($_GET['mensaje'] === 'producto_creado') {
 echo '<div class="mensaje exito"> Producto creado exitosamente</div>' ✅ ;
 } elseif ($_GET['mensaje'] === 'producto_eliminado') {
 echo '<div class="mensaje exito"> Producto eliminado exitosamente</div>' ✅ ;
 }
}
?>
<h2>Lista de Productos</h2>
<?php if (empty($productos)): ?>
 <p>No hay productos registrados. <a href="index.php?accion=crear">Crear el
primero</a></p>
<?php else: ?>
 <table>
 <thead>
 <tr>
 <th>ID</th>
 <th>Nombre</th>
 <th>Precio</th>
 <th>Stock</th>
 <th>Fecha</th>
 <th>Acciones</th>
 </tr>
 </thead>
 <tbody>
 <?php foreach ($productos as $prod): ?>
 <tr>
 <td><?php echo $prod['id']; ?></td>
 <td><?php echo htmlspecialchars($prod['nombre']); ?></td>
 <td><?php echo number_format($prod['precio'], 2); ?> €</td>
 <td><?php echo $prod['stock']; ?> unidades</td>
 <td><?php echo date('d/m/Y', strtotime($prod['fecha_creacion'])); ?
></td>
 <td>
 <a href="index.php?accion=detalle&id=<?php echo $prod['id']; ?>"
class="btn btn-primary">Ver</a>
 <form method="POST" action="index.php?accion=eliminar"
style="display: inline;">
 <input type="hidden" name="id" value="<?php echo $prod['id']; ?
>">
 <button type="submit" class="btn btn-danger"
 onclick="return confirm('¿Estás seguro de eliminar este
producto?')">
 Eliminar
 </button>
 </form>
 </td>
 </tr>
 <?php endforeach; ?>
 </tbody>
 </table>
<?php endif; ?>
<?php require_once 'views/layout/footer.php'; ?>