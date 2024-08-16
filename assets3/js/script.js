var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjeta de crédito" }
]

//Formulario
let form = document.getElementById("formulario");
let btnNew = document.getElementById("btnNew");
let newTxt = document.getElementById("nuevaTarea");
let btnAdd = document.getElementById("btnAdd");

//Tabla
let tBody = document.getElementById("cuerpo-tabla");


//"Agregar tarea" despliega text input
btnNew.addEventListener('click', function () {
    form.style.display = "block";
})

//Función que toma la información de la tabla y la actualiza

function tUpdate() {
    tBody.innerHTML = '';
    tareas.forEach(function (tareaObj) {
        const row = document.createElement('tr');
        const data = document.createElement('td');
        const finish = document.createElement('td');
        const btnFinish = document.createElement('button');
        data.textContent = tareaObj.tarea;
        btnFinish.setAttribute('class', 'btn btn-danger');
        btnFinish.textContent = "Finalizar";
        finish.appendChild(btnFinish);
        row.appendChild(data);
        row.appendChild(finish);
        tBody.appendChild(row);
    });
}

//"Agregar" introduce el text input en la tabla/lista
btnAdd.addEventListener('click', function () {
    if (newTxt.value.trim() !== ''){
        tareas.push({tarea: newTxt.value});
        tUpdate();
        form.style.display = "none";
        newTxt.value = '';
    }
})

//Boton "finalizar" para borrar elementos de la tabla/lista

tUpdate()