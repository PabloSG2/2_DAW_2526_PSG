<?php require_once 'views/layout/header.php'; ?>
<h2>Detalle del Producto</h2>
<div class="detalle-card">
 <h3><?php echo htmlspecialchars($this->producto->nombre); ?></h3>
 <p><strong>ID:</strong> <?php echo $this->producto->id; ?></p>
 <p><strong>Descripción:</strong> <?php echo htmlspecialchars($this->producto-
>descripcion); ?></p>
 <p><strong>Precio:</strong> <?php echo number_format($this->producto->precio, 2); ?>
€</p>
 <p><strong>Stock:</strong> <?php echo $this->producto->stock; ?> unidades</p>
 <p><strong>Fecha de creación:</strong> <?php echo date('d/m/Y H:i', strtotime($this-
>producto->fecha_creacion)); ?></p>

 <br>
 <a href="index.php" class="btn btn-primary">↩️ Volver al Listado</a>
</div>
<?php require_once 'views/layout/footer.php'; ?>