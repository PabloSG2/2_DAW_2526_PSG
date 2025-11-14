<!DOCTYPE html>
<html>

<head>
</head>

<body>
    <h1>Datos:</h1>
    <?php
    echo '<p>Codigo=' . $_GET['tipo'] . '</p>';
    echo '<p>Nombre=' . $_GET['nom'] . '</p>';
    echo '<p>Edad=' . $_GET['edad'] . '</p>';
    ?>
    <h2>Añadiendo datos...</h2>
    <?php
    $con = mysqli_connect('localhost', 'd24pablo_prueba', '1234', 'd24pablo_bd');
    $pre = mysqli_prepare($con, 'INSERT INTO tabla (tipo,nombre,edad) VALUES (?,?,?)');
    mysqli_stmt_bind_param(
        $pre,
        "ssi",
        $_GET['tipo'],
        $_GET['nom'],
        $_GET['edad']
    );
    mysqli_stmt_execute($pre);
    ?>
    <h2>Ver datos:</h2>
    Id,Tipo,Nombre,Edad<br>
    <?php
    $sql = 'SELECT * FROM tabla;';
    $result = mysqli_query($con, $sql);
    while ($fila = mysqli_fetch_array($result)) {
        echo $fila['id'] . ',' . $fila['tipo'] . ',' .
            $fila['nombre'] . ',' . $fila['edad'] . '<br>';
    }
    mysqli_close($con);
    ?>
</body>

</html>