window.addEventListener("DOMContentLoaded", function() {
  // Pedimos al usuario los índices de productos que desea ver
  let seleccion = prompt("Escribe los números de los productos separados por comas (ej: 0,1,2):");2

  // Lista de productos disponibles
  let productos = [
    { imagen: 'pro1.png', nombre: 'Incienso Tres Reyes' },
    { imagen: 'pro2.png', nombre: 'Incienso Noches de Bronce' },
    { imag2en: '', nombre: 'Producto Extra sin foto' }
  ];

  // Obtenemos el contenedor donde se insertarán las tarjetas
  let contenedor = document.getElementById('cardsContainer');
  if (!contenedor) return; // Si no existe, salimos

  // Recorremos cada número ingresado por el usuario
  seleccion.split(',').forEach(function(num) {
    let i = parseInt(num); // Convertimos el string a número
    let p = productos[i];  // Obtenemos el producto por índice

    // Creamos la tarjeta
    let card = document.createElement('div');
    card.className = 'card';

    // Creamos y configuramos la imagen
    let img = document.createElement('img');
    img.src = p ? (p.imagen ? '../IMG/' + p.imagen : '../IMG/noencontrado.png') : '../IMG/noencontrado.png';

    // Creamos el texto con el nombre del producto o mensaje de error
    let texto = document.createElement('p');
    texto.textContent = p ? p.nombre : 'Producto no encontrado';

    // Agregamos imagen y texto a la tarjeta
    card.appendChild(img);
    card.appendChild(texto);

    // Insertamos la tarjeta en el contenedor
    contenedor.appendChild(card);
  });
});