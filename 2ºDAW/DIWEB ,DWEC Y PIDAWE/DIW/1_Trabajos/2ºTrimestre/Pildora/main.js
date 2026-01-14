// ===================== OBTENER ELEMENTOS DEL VIDEO =====================
// Obtiene el elemento del video
const video = document.getElementById("video");

// Botones del video
const playBtn = document.getElementById("play");
const muteBtn = document.getElementById("mute");
const pipBtn = document.getElementById("pip");
const fullscreenBtn = document.getElementById("fullscreen");

// Barra de progreso del video
const progress = document.getElementById("progress");
const progressBar = document.getElementById("progress-bar");

// Controles de tiempo del video
const currentTimeEl = document.getElementById("current");
const durationEl = document.getElementById("duration");

// Control de volumen del video
const volumeSlider = document.getElementById("volume");

// ===================== FUNCIÓN GENERAL PARA AUDIO Y VIDEO =====================
function setupMediaProgress(media, progressContainer, progressBar, currentEl, durationEl) {

    // Cuando se cargan los metadatos (duración total)
    media.addEventListener("loadedmetadata", () => {
        durationEl.textContent = formatTime(media.duration); // Muestra duración formateada
    });

    // Mientras avanza el tiempo de reproducción
    media.addEventListener("timeupdate", () => {
        currentEl.textContent = formatTime(media.currentTime); // Actualiza tiempo actual

        const percent = (media.currentTime / media.duration) * 100; // Calcula porcentaje
        progressBar.style.width = percent + "%"; // Ajusta la barra
    });

    // Cuando el usuario hace clic en la barra de progreso
    progressContainer.addEventListener("click", (e) => {
        const rect = progressContainer.getBoundingClientRect(); // Tamaño de la barra
        const clickX = e.clientX - rect.left; // Posición del clic
        media.currentTime = (clickX / rect.width) * media.duration; // Salta al tiempo correspondiente
    });
}

// ===================== APLICAR FUNCIÓN AL VIDEO =====================
setupMediaProgress(
    video,
    progress,
    progressBar,
    currentTimeEl,
    durationEl
);

// ===================== CONTROLES DEL VIDEO =====================
// Botón play/pause
playBtn.addEventListener("click", () => {
    video.paused ? video.play() : video.pause(); // Alterna reproducción
});

// Cambia icono al reproducir
video.addEventListener("play", () => playBtn.textContent = "⏸️");

// Cambia icono al pausar
video.addEventListener("pause", () => playBtn.textContent = "▶️");

// Botón mute
muteBtn.addEventListener("click", () => {
    video.muted = !video.muted; // Alterna mute
    muteBtn.textContent = video.muted ? "🔊" : "🔇"; // Cambia icono
});

// Control de volumen
volumeSlider.addEventListener("input", () => {
    video.volume = volumeSlider.value; // Ajusta volumen
});

// Picture-in-Picture
pipBtn.addEventListener("click", async () => {
    if (document.pictureInPictureElement) {
        await document.exitPictureInPicture(); // Sale de PiP
    } else {
        await video.requestPictureInPicture(); // Entra en PiP
    }
});

// Pantalla completa
fullscreenBtn.addEventListener("click", () => {
    if (!document.fullscreenElement) {
        video.requestFullscreen(); // Entra en fullscreen
    } else {
        document.exitFullscreen(); // Sale
    }
});

// ===================== FORMATEAR TIEMPO =====================
function formatTime(time) {
    const m = Math.floor(time / 60); // Minutos
    const s = Math.floor(time % 60).toString().padStart(2, "0"); // Segundos con 0 delante
    return `${m}:${s}`; // Devuelve formato mm:ss
}

// ===================== IMAGEN EDITABLE =====================
// Obtiene la imagen editable
const editableImg = document.getElementById("editable-img");

// Valores iniciales
let scale = 1;
let opacity = 1;
let rotation = 0;

// Botón zoom
document.getElementById("zoom").onclick = () => {
    scale += 0.2; // Aumenta zoom
    updateImage(); // Actualiza imagen
};

// Botón opacidad
document.getElementById("opacity").onclick = () => {
    opacity -= 0.1; // Reduce opacidad
    if (opacity < 0.2) opacity = 1; // Reinicia si es muy baja
    updateImage();
};

// Botón rotar
document.getElementById("rotate").onclick = () => {
    rotation += 15; // Aumenta rotación
    updateImage();
};

// Botón reset
document.getElementById("reset").onclick = () => {
    scale = 1;
    opacity = 1;
    rotation = 0;
    updateImage();
};

// Aplica cambios visuales a la imagen
function updateImage() {
    editableImg.style.transform = `scale(${scale}) rotate(${rotation}deg)`; // Zoom + rotación
    editableImg.style.opacity = opacity; // Opacidad
}

// ===================== AUDIO AVANZADO =====================
// Obtiene el audio
const audio2 = document.getElementById("audio2");

// Botón play/pause del audio
const audioPlayBtn = document.getElementById("audioPlay");

// Control de velocidad
const speedControl = document.getElementById("speed");

// Reproducir/pausar audio
audioPlayBtn.addEventListener("click", () => {
    audio2.paused ? audio2.play() : audio2.pause();
});

// Cambia icono al reproducir
audio2.addEventListener("play", () => audioPlayBtn.textContent = "⏸️");

// Cambia icono al pausar
audio2.addEventListener("pause", () => audioPlayBtn.textContent = "▶️");

// Control de velocidad
speedControl.addEventListener("input", () => {
    audio2.playbackRate = speedControl.value; // Cambia velocidad
});

// Obtenemos el botón de loop
const loopBtn = document.getElementById("loopBtn");

// Establecemos el estado inicial del loop en falso (no repetir)
audio2.loop = false;

// Mostramos el texto inicial del botón acorde al estado
loopBtn.textContent = "🔁 Loop OFF";

// Evento al hacer clic en el botón de loop
loopBtn.addEventListener("click", () => {
    // Alternamos el valor del loop: si estaba en false pasa a true, y viceversa
    audio2.loop = !audio2.loop;
    // Cambiamos el texto del botón según el nuevo estado
    loopBtn.textContent = audio2.loop
        ? "🔂 Loop ON"   // Si está activado
        : "🔁 Loop OFF"; // Si está desactivado
});

// ===================== APLICAR FUNCIÓN AL AUDIO =====================
setupMediaProgress(
    audio2,
    document.getElementById("audioProgress"),
    document.getElementById("audioProgressBar"),
    document.getElementById("audioCurrent"),
    document.getElementById("audioDuration")
);