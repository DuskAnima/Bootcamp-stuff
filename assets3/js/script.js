var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
]

let form = document.getElementById("formulario");
let btnNew = document.getElementById("btnNew");
let btnAdd = document.getElementById("btnAdd");
let newTxt = document.getElementById("nuevaTarea");
let tableBody = document.getElementById("cuerpo-tabla");

const row = document.createElement('tr')

// "Agregar tarea" despliega text input
btnNew.addEventListener('click', function(){
    form.style.display = "block";
})

// "Agregar" introduce el text input en la tabla/lista
btnAdd.addEventListener('click', function(){
    form.style.display = "none";
})