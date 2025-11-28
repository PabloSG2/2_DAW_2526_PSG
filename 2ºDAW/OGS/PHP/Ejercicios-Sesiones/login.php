<form method="post">
    Usuario: <input type="text" name="usuario">
    Constraseña: <input type="password" name="pass">
    <input type="submit" name="login" value="Login">
</form>

<?php
if (isset($_POST["login"])) {
    if (!empty($_POST["Usuario"]) && !empty($_POST["pass"])) {
        $usuario= $_POST["usuario"];
        $pass = $_POST["pass"];

        if ($usuario == "admin" AND $pass == "root") {
            header("");
        }
    }else {
        echo "Usuario/constraseña incorrecto";
    }
}

?>