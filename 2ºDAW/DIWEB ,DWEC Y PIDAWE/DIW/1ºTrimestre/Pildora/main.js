const video = document.getElementById("video");
const playBtn = document.getElementById("play");
const pipBtn = document.getElementById("pip");
const progress = document.getElementById("progress");
const progressBar = document.getElementById("progress-bar");

// Play/Pause
playBtn.addEventListener("click", () => {
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
});

// Actualizar barra de progreso
video.addEventListener("timeupdate", () => {
  const percent = (video.currentTime / video.duration) * 100;
  progressBar.style.width = percent + "%";
});

// Saltar en el vídeo al hacer clic en la barra
progress.addEventListener("click", (e) => {
  const rect = progress.getBoundingClientRect();
  const clickX = e.clientX - rect.left;
  const newTime = (clickX / rect.width) * video.duration;
  video.currentTime = newTime;
});

// Picture-in-Picture
pipBtn.addEventListener("click", async () => {
  try {
    await video.requestPictureInPicture();
  } catch (err) {
    console.error("Error al activar PiP:", err);
  }
});


