// ===================== CONTROL DE VIDEO =====================

// Obtiene el elemento <video> que tendrá controles personalizados
const video = document.getElementById("video");

// Obtiene el botón Play/Pause
const playBtn = document.getElementById("play");

// Obtiene el botón Picture-in-Picture
const pipBtn = document.getElementById("pip");

// Obtiene el contenedor de la barra de progreso
const progress = document.getElementById("progress");

// Obtiene la barra interna que se llenará según el avance del vídeo
const progressBar = document.getElementById("progress-bar");


// --------------------- PLAY / PAUSE ---------------------

// Evento que se ejecuta cuando se hace clic en el botón Play/Pause
playBtn.addEventListener("click", () => {

    // Si el vídeo está pausado, lo reproduce
    if (video.paused) {
        video.play();

    // Si está reproduciéndose, lo pausa
    } else {
        video.pause();
    }
});


// --------------------- ACTUALIZAR BARRA DE PROGRESO ---------------------

// Evento que se ejecuta cada vez que cambia el tiempo del vídeo
video.addEventListener("timeupdate", () => {

    // Comprueba que el vídeo tiene duración válida
    if (video.duration) {

        // Calcula el porcentaje reproducido (tiempo actual / duración total)
        const percent = (video.currentTime / video.duration) * 100;

        // Ajusta el ancho de la barra azul según el porcentaje
        progressBar.style.width = percent + "%";
    }
});


// --------------------- SALTAR A UNA PARTE DEL VIDEO ---------------------

// Evento cuando el usuario hace clic en la barra de progreso
progress.addEventListener("click", (e) => {

    // Obtiene tamaño y posición de la barra en pantalla
    const rect = progress.getBoundingClientRect();

    // Calcula la posición exacta donde el usuario hizo clic
    const clickX = e.clientX - rect.left;

    // Convierte esa posición en tiempo del vídeo
    const newTime = (clickX / rect.width) * video.duration;

    // Cambia el tiempo actual del vídeo al nuevo tiempo calculado
    video.currentTime = newTime;
});


// --------------------- PICTURE-IN-PICTURE ---------------------

// Evento para activar/desactivar el modo PiP
pipBtn.addEventListener("click", async () => {

    try {
        // Si ya está en modo PiP, lo cierra
        if (document.pictureInPictureElement) {
            await document.exitPictureInPicture();

        // Si no está en PiP, lo activa
        } else {
            await video.requestPictureInPicture();
        }

    } catch (error) {
        // Si ocurre un error, lo muestra en consola
        console.error("Error al activar Picture-in-Picture", error);
    }
});


// ===================== IMAGEN MODIFICABLE =====================

// Obtiene la imagen editable
const editableImg = document.getElementById("editable-img");

// Variables que guardan el estado actual de la imagen
let scale = 1;   // Tamaño inicial (1 = normal)
let opacity = 1; // Opacidad inicial (1 = totalmente visible)


// --------------------- BOTÓN ZOOM ---------------------

// Evento cuando se pulsa el botón Zoom
document.getElementById("zoom").addEventListener("click", () => {

    // Aumenta el tamaño en 0.2 cada vez
    scale += 0.2;

    // Aplica los cambios a la imagen
    updateImage();
});


// --------------------- BOTÓN OPACIDAD ---------------------

// Evento cuando se pulsa el botón Opacidad
document.getElementById("opacity").addEventListener("click", () => {

    // Reduce la opacidad en 0.1
    opacity -= 0.1;

    // Si llega a menos de 0.2, la reinicia a 1
    if (opacity < 0.2) opacity = 1;

    // Aplica los cambios
    updateImage();
});


// --------------------- BOTÓN RESET ---------------------

// Evento cuando se pulsa el botón Reset
document.getElementById("reset").addEventListener("click", () => {

    // Restaura valores originales
    scale = 1;
    opacity = 1;

    // Aplica los cambios
    updateImage();
});


// --------------------- FUNCIÓN QUE ACTUALIZA LA IMAGEN ---------------------

function updateImage() {

    // Aplica el zoom usando transform: scale()
    editableImg.style.transform = `scale(${scale})`;

    // Aplica la opacidad
    editableImg.style.opacity = opacity;
}
