<!DOCTYPE html>
<html lang="es">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Gestión de Productos</title>
 <style>
 * { margin: 0; padding: 0; box-sizing: border-box; }
 body { font-family: Arial, sans-serif; background: #f4f4f4; }
 .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
 header { background: #333; color: white; padding: 20px 0; margin-bottom: 30px; }
 header h1 { text-align: center; }
 nav { background: #555; padding: 10px; margin-bottom: 20px; text-align: center; }
 nav a { color: white; text-decoration: none; padding: 10px 20px; display: inlineblock; }
 nav a:hover { background: #777; }
 .mensaje { padding: 15px; margin-bottom: 20px; border-radius: 5px; }
 .mensaje.exito { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
 .mensaje.error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
 table { width: 100%; background: white; border-collapse: collapse; box-shadow: 0 2px
5px rgba(0,0,0,0.1); }
 th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
 th { background: #333; color: white; }
 .btn { padding: 8px 16px; text-decoration: none; border-radius: 4px; display:
inline-block; border: none; cursor: pointer; }
 .btn-primary { background: #007bff; color: white; }
 .btn-success { background: #28a745; color: white; }
 .btn-danger { background: #dc3545; color: white; }
 .btn:hover { opacity: 0.8; }
 form { background: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px
rgba(0,0,0,0.1); }
 .form-group { margin-bottom: 15px; }
 label { display: block; margin-bottom: 5px; font-weight: bold; }
 input, textarea { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius:
4px; }
 .detalle-card { background: white; padding: 20px; border-radius: 5px; box-shadow: 0
2px 5px rgba(0,0,0,0.1); }
 </style>
</head>
<body>
 <header>
 <h1>🛒 Sistema de Gestión de Productos</h1>
 </header>
 <nav>
 <a href="index.php">📋 Inicio</a>
 <a href="index.php?accion=crear">➕ Nuevo Producto</a>
 </nav>
 <div class="container">
