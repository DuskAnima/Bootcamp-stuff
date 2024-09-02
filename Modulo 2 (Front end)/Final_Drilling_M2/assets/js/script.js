//JS vanilla stuff

document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const gradientBg = document.createElement('div');
    gradientBg.id = 'gradient-bg';
    body.appendChild(gradientBg);

    body.addEventListener('mousemove', (e) => {
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        const gradientSize = 150; // Tamaño del radio del gradiente

        gradientBg.style.background = `radial-gradient(circle at ${mouseX}px ${mouseY}px, #00d4ff, #090979, #020024 ${gradientSize}px)`;
        gradientBg.style.opacity = 1; // Hacer visible el fondo gradiente
    });

    body.addEventListener('mouseleave', () => {
        gradientBg.style.opacity = 0; // Hacer invisible el fondo gradiente al salir del área
    });
});

//jQuery stuff


$(document).ready(function () {
    $('#tech > h2').click(function () {
        $(this).next('ul').slideToggle('fast'); // Despliega o contrae el ul siguiente
        $(this).toggleClass('open'); // Añade o elimina la clase 'open' al h2 clickeado
    });
});

