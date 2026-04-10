/*função para o temporizador ~emanuel*/

document.addEventListener("DOMContentLoaded", function () {
  
  const display = document.getElementsByClassName("timer")[0];

  if (!display) return;

  const countDownDate = new Date(display.getAttribute("data-target")).getTime();
  
  const x = setInterval(function() {
        const now = new Date().getTime();
        
        // Encontra a diferença entre agora e a data alvo
        const distance = countDownDate - now;

        // Cálculos matemáticos para dias, horas, minutos e segundos
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));

        // Mostra o resultado na div (essa parte editei por mim mesmo ~emanuel)
        if (days > 0) {
          display.innerHTML = days + "d" + hours + "h";
        } else if (hours < 10 && minutes < 10) {
          display.innerHTML = "0" + hours + ":0" + minutes;
        } else if (hours < 10) {
          display.innerHTML = "0" + hours + ":" + minutes;
        } else if (minutes < 10) {
          display.innerHTML = hours + ":0" + minutes;
        } else {
          display.innerHTML = hours + ":" + minutes;
        }

        // Se o tempo acabar, para o timer e mostra uma mensagem
        if (distance < 0) {
            clearInterval(x);
            display.innerHTML = "00:00";
        }
    }, 1000);
});