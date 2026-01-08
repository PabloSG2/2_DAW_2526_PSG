// Obtiene el elemento de vídeo del HTML
const video = document.getElementById("video");

// Botón Play / Pause
const playBtn = document.getElementById("play");

// Botón Picture-in-Picture
const pipBtn = document.getElementById("pip");

// Barra de progreso (contenedor)
const progress = document.getElementById("progress");

// Barra que indica el avance del vídeo
const progressBar = document.getElementById("progress-bar");


// ===================== PLAY / PAUSE =====================
playBtn.addEventListener("click", () => {
  // Si el vídeo está en pausa, se reproduce
  if (video.paused) {
    video.play();
  } else {
    // Si está reproduciéndose, se pausa
    video.pause();
  }
});


// ===================== ACTUALIZAR BARRA =====================
video.addEventListener("timeupdate", () => {
  // Comprueba que el vídeo tiene duración
  if (video.duration) {
    // Calcula el porcentaje reproducido
    const percent = (video.currentTime / video.duration) * 100;

    // Ajusta el ancho de la barra de progreso
    progressBar.style.width = percent + "%";
  }
});


// ===================== SALTAR EN EL VÍDEO =====================
progress.addEventListener("click", (e) => {
  // Obtiene el tamaño y posición de la barra
  const rect = progress.getBoundingClientRect();

  // Calcula la posición del clic
  const clickX = e.clientX - rect.left;

  // Convierte la posición en tiempo del vídeo
  const newTime = (clickX / rect.width) * video.duration;

  // Cambia el tiempo actual del vídeo
  video.currentTime = newTime;
});


// ===================== PICTURE-IN-PICTURE =====================
pipBtn.addEventListener("click", async () => {
  try {
    // Si ya está en modo PiP, sale
    if (document.pictureInPictureElement) {
      await document.exitPictureInPicture();
    } else {
      // Si no está en PiP, lo activa
      await video.requestPictureInPicture();
    }
  } catch (error) {
    // Muestra errores en consola
    console.error("Error al activar Picture-in-Picture", error);
  }
});
