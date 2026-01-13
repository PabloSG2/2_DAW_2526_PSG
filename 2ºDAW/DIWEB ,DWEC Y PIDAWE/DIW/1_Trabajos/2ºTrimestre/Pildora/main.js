// ===================== VIDEO PERSONALIZADO =====================
// Obtiene el elemento de video principal
const video = document.getElementById("video");

// Obtiene el botón de reproducir/pausar
const playBtn = document.getElementById("play");

// Obtiene el botón de mute/unmute
const muteBtn = document.getElementById("mute");

// Obtiene el botón de Picture-in-Picture
const pipBtn = document.getElementById("pip");

// Obtiene el botón de pantalla completa
const fullscreenBtn = document.getElementById("fullscreen");

// Obtiene el contenedor de la barra de progreso
const progress = document.getElementById("progress");

// Obtiene la barra interna que muestra el avance
const progressBar = document.getElementById("progress-bar");

// Obtiene el control deslizante del volumen
const volumeSlider = document.getElementById("volume");

// Obtiene el elemento donde se muestra el tiempo actual
const currentTimeEl = document.getElementById("current");

// Obtiene el elemento donde se muestra la duración total
const durationEl = document.getElementById("duration");


// --------------------- PLAY / PAUSE ---------------------
// Evento al hacer clic en el botón play
playBtn.addEventListener("click", () => {
    // Si el video está pausado, lo reproduce; si no, lo pausa
    video.paused ? video.play() : video.pause();
});

// Evento cuando el video empieza a reproducirse
video.addEventListener("play", () => playBtn.textContent = "⏸️");

// Evento cuando el video se pausa
video.addEventListener("pause", () => playBtn.textContent = "▶️");


// --------------------- MUTE ---------------------
// Evento al hacer clic en el botón de mute
muteBtn.addEventListener("click", () => {
    // Cambia el estado de mute del video
    video.muted = !video.muted;

    // Cambia el icono según si está muteado o no
    muteBtn.textContent = video.muted ? "🔊" : "🔇";
});


// --------------------- VOLUMEN ---------------------
// Evento al mover el slider de volumen
volumeSlider.addEventListener("input", () => {
    // Asigna el valor del slider al volumen del video
    video.volume = volumeSlider.value;
});


// --------------------- TIEMPOS ---------------------
// Evento cuando se cargan los metadatos del video (duración, etc.)
video.addEventListener("loadedmetadata", () => {
    // Muestra la duración total formateada
    durationEl.textContent = formatTime(video.duration);
});

// Evento que se ejecuta mientras el video avanza
video.addEventListener("timeupdate", () => {
    // Actualiza el tiempo actual formateado
    currentTimeEl.textContent = formatTime(video.currentTime);

    // Calcula el porcentaje reproducido
    const percent = (video.currentTime / video.duration) * 100;

    // Ajusta el ancho de la barra de progreso
    progressBar.style.width = percent + "%";
});


// --------------------- BARRA DE PROGRESO ---------------------
// Evento al hacer clic en la barra de progreso
progress.addEventListener("click", (e) => {
    // Obtiene la posición y tamaño de la barra
    const rect = progress.getBoundingClientRect();

    // Calcula la posición del clic dentro de la barra
    const clickX = e.clientX - rect.left;

    // Calcula el tiempo correspondiente al clic
    video.currentTime = (clickX / rect.width) * video.duration;
});


// --------------------- PICTURE IN PICTURE ---------------------
// Evento al hacer clic en el botón PiP
pipBtn.addEventListener("click", async () => {
    // Si ya está en PiP, sale
    if (document.pictureInPictureElement) {
        await document.exitPictureInPicture();
    } else {
        // Si no, entra en PiP
        await video.requestPictureInPicture();
    }
});


// --------------------- FULLSCREEN ---------------------
// Evento al hacer clic en el botón de pantalla completa
fullscreenBtn.addEventListener("click", () => {
    // Si no está en pantalla completa
    if (!document.fullscreenElement) {
        // Entra en pantalla completa
        video.requestFullscreen();
    } else {
        // Si ya está, sale
        document.exitFullscreen();
    }
});


// --------------------- FUNCIÓN FORMATO TIEMPO ---------------------
// Convierte segundos a formato mm:ss
function formatTime(time) {
    // Calcula los minutos
    const m = Math.floor(time / 60);

    // Calcula los segundos y los rellena con 0 si hace falta
    const s = Math.floor(time % 60).toString().padStart(2, "0");

    // Devuelve el tiempo formateado
    return `${m}:${s}`;
}


// ===================== IMAGEN EDITABLE =====================
// Obtiene la imagen editable
const editableImg = document.getElementById("editable-img");

// Valor inicial del zoom
let scale = 1;

// Valor inicial de la opacidad
let opacity = 1;

// Valor inicial de la rotación
let rotation = 0;

// Evento al hacer clic en el botón de zoom
document.getElementById("zoom").onclick = () => {
    // Aumenta el zoom
    scale += 0.2;

    // Actualiza la imagen
    updateImage();
};

// Evento al hacer clic en el botón de opacidad
document.getElementById("opacity").onclick = () => {
    // Reduce la opacidad
    opacity -= 0.1;

    // Si baja demasiado, vuelve a 1
    if (opacity < 0.2) opacity = 1;

    // Actualiza la imagen
    updateImage();
};

// Evento al hacer clic en el botón de rotar
document.getElementById("rotate").onclick = () => {
    // Aumenta la rotación en 15 grados
    rotation += 15;

    // Actualiza la imagen
    updateImage();
};

// Evento al hacer clic en el botón reset
document.getElementById("reset").onclick = () => {
    // Restaura los valores iniciales
    scale = 1;
    opacity = 1;
    rotation = 0;

    // Actualiza la imagen
    updateImage();
};

// Función que aplica los cambios visuales a la imagen
function updateImage() {
    // Aplica zoom y rotación
    editableImg.style.transform = `scale(${scale}) rotate(${rotation}deg)`;

    // Aplica opacidad
    editableImg.style.opacity = opacity;
}


// ===================== AUDIO AVANZADO =====================
// Obtiene el elemento del audio avanzado
const audio2 = document.getElementById("audio2");

// Obtiene el botón de reproducción/pausa
const audioPlayBtn = document.getElementById("audioPlay");

// Obtiene el control deslizante de velocidad
const speedControl = document.getElementById("speed");

// Obtiene el control deslizante de tono
const pitchControl = document.getElementById("pitch");

// --------------------- PLAY / PAUSE ---------------------
// Evento al hacer clic en el botón de play/pause
audioPlayBtn.addEventListener("click", () => {
    // Si el audio está pausado, lo reproduce; si no, lo pausa
    audio2.paused ? audio2.play() : audio2.pause();
});

// --------------------- CONTROL DE TONO ---------------------
// Evento al mover el slider de tono
pitchControl.addEventListener("input", () => {
    // Permite modificar el tono real del audio
    audio2.preservesPitch = false;

    // Ajusta el tono modificando la velocidad de reproducción
    audio2.playbackRate = pitchControl.value;
});

// --------------------- CAMBIO DE ICONOS ---------------------
// Cuando el audio empieza a reproducirse, cambia el icono a pausa y play
audio2.addEventListener("play", () => audioPlayBtn.textContent = "⏸️");
audio2.addEventListener("pause", () => audioPlayBtn.textContent = "▶️");

// --------------------- CONTROL DE VELOCIDAD ---------------------
// Evento al mover el slider de velocidad
speedControl.addEventListener("input", () => {
    // Cambia la velocidad de reproducción del audio
    audio2.playbackRate = speedControl.value;
});
