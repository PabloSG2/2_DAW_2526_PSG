<?php require_once 'views/layout/header.php'; ?>
<h2>Crear Nuevo Producto</h2>
<?php if (isset($error)): ?>
 <div class="mensaje error">❌ <?php echo $error; ?></div>
<?php endif; ?>
<form method="POST" action="index.php?accion=guardar">
 <div class="form-group">
 <label for="nombre">Nombre del Producto *</label>
 <input type="text" id="nombre" name="nombre" required>
 </div>
 <div class="form-group">
 <label for="descripcion">Descripción</label>
 <textarea id="descripcion" name="descripcion" rows="4"></textarea>
 </div>
 <div class="form-group">
 <label for="precio">Precio (€) *</label>
 <input type="number" id="precio" name="precio" step="0.01" min="0" required>
 </div>
 <div class="form-group">
 <label for="stock">Stock *</label>
 <input type="number" id="stock" name="stock" min="0" required>
 </div>
 <button type="submit" class="btn btn-success">💾 Guardar Producto</button>
 <a href="index.php" class="btn btn-primary">↩️ Volver</a>
</form>
<?php require_once 'views/layout/footer.php'; ?>
