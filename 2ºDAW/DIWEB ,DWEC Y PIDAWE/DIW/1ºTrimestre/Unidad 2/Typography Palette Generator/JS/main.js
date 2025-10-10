// Esperamos a que el documento HTML haya cargado completamente
document.addEventListener("DOMContentLoaded", () => {

  // Referencia al elemento raíz del documento (:root), donde están las variables CSS
  const root = document.documentElement;

  // Referencias a los campos de color del formulario
  const colorBg = document.getElementById("color-bg");        // Selector de color de fondo
  const colorFg = document.getElementById("color-fg");        // Selector de color de texto
  const colorPrimary = document.getElementById("color-primary"); // Selector de color primario (acento)

  // Referencias a los campos de tipografía
  const fontSans = document.getElementById("font-sans");      // Selector de familia tipográfica
  const fontWeight = document.getElementById("font-weight");  // Selector de peso tipográfico

  // Referencias a los botones de acción del formulario
  const copyButton = document.getElementById("copy-vars");    // Botón para copiar las variables
  const resetButton = document.getElementById("reset-vars");  // Botón para restablecer los valores

  // Guardamos los valores iniciales para poder restablecerlos más tarde
  const defaultVars = {
    bg: colorBg.value,          // Color de fondo por defecto
    fg: colorFg.value,          // Color de texto por defecto
    primary: colorPrimary.value, // Color primario por defecto
    font: fontSans.value,       // Familia tipográfica por defecto
    weight: fontWeight.value    // Peso tipográfico por defecto
  };

  // Función que actualiza las variables CSS según los valores elegidos por el usuario
  function updateCSSVars() {
    root.style.setProperty("--color-bg", colorBg.value);          // Actualiza el color de fondo
    root.style.setProperty("--color-fg", colorFg.value);          // Actualiza el color del texto
    root.style.setProperty("--color-primary", colorPrimary.value); // Actualiza el color primario
    root.style.setProperty("--font-sans", fontSans.value);        // Actualiza la familia tipográfica
    root.style.setProperty("--font-weight", fontWeight.value);    // Actualiza el peso tipográfico

    // Antes: se aplicaba el peso al body entero
    // document.body.style.fontWeight = fontWeight.value;
    // Ahora lo quitamos para que solo afecte a los elementos que usen la variable CSS
  }

  // Función para copiar las variables CSS actuales al portapapeles
  function copyCSSVars() {
    // Creamos una cadena con el formato CSS de las variables
    const cssVars =
`:root {
  --color-bg: ${colorBg.value};
  --color-fg: ${colorFg.value};
  --color-primary: ${colorPrimary.value};
  --font-sans: ${fontSans.value};
  --font-weight: ${fontWeight.value};
}`;

    // Copiamos el texto generado al portapapeles del usuario
    navigator.clipboard.writeText(cssVars)
      .then(() => alert("Variables copiadas al portapapeles")) // Si se copia correctamente, muestra mensaje
      .catch(() => alert("No se pudo copiar al portapapeles")); // Si falla, muestra mensaje de error
  }

  // Función para restablecer los valores del formulario a los originales
  function resetVars() {
    colorBg.value = defaultVars.bg;            // Restaura el color de fondo
    colorFg.value = defaultVars.fg;            // Restaura el color de texto
    colorPrimary.value = defaultVars.primary;  // Restaura el color primario
    fontSans.value = defaultVars.font;         // Restaura la familia tipográfica
    fontWeight.value = defaultVars.weight;     // Restaura el peso tipográfico

    updateCSSVars();                           // Aplica los valores por defecto
  }

  // Escuchadores de eventos para detectar cambios y aplicar la actualización
  colorBg.addEventListener("input", updateCSSVars);        // Cuando cambia el color de fondo
  colorFg.addEventListener("input", updateCSSVars);        // Cuando cambia el color del texto
  colorPrimary.addEventListener("input", updateCSSVars);   // Cuando cambia el color primario
  fontSans.addEventListener("change", updateCSSVars);      // Cuando cambia la familia tipográfica
  fontWeight.addEventListener("change", updateCSSVars);    // Cuando cambia el peso tipográfico

  // Escuchadores para los botones
  copyButton.addEventListener("click", copyCSSVars);       // Al hacer clic en "Copiar variables"
  resetButton.addEventListener("click", resetVars);        // Al hacer clic en "Restablecer"

  // Llamamos a la función al iniciar para aplicar los valores actuales
  updateCSSVars();
});

