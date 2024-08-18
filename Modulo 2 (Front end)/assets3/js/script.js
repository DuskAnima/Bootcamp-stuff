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
function ListUpdate() {
    tBody.innerHTML = '';
    tareas.forEach(function (tareaObj, index) {
        const row = document.createElement('tr');
        const data = document.createElement('td');
        const finish = document.createElement('td');
        const btnFinish = document.createElement('button');
        data.textContent = tareaObj.tarea;
        btnFinish.setAttribute('class', 'btn btn-danger');
        btnFinish.setAttribute('onclick', `removeTask(${index})`);
        btnFinish.textContent = "Finalizar";
        finish.appendChild(btnFinish);
        row.appendChild(data);
        row.appendChild(finish);
        tBody.appendChild(row);
    });
}

//Botón"Agregar" e input key "Enter" introduce el text input en la tabla/lista
function addTask() {
    if (newTxt.value.trim() !== '') {
        tareas.push({ tarea: newTxt.value });
        ListUpdate();
        form.style.display = "none";
        newTxt.value = '';
    }
}

btnAdd.addEventListener('click', addTask);

newTxt.addEventListener('keydown', function(event){
    if (event.key === 'Enter'){
        event.preventDefault();
        addTask();
    }
});

//Boton "finalizar" para borrar elementos de la tabla/lista
function removeTask(index) {
    tareas.splice(index, 1)
    ListUpdate()
}


ListUpdate()


/* 
Funcionamiento del flujo de datos para crear y eliminar objetos de la lista:

-> En ListUpdate():

-> tareas.forEach(function (tareaObj, index)  le da un nombre de variable al objeto concreto y le asigna una posición en la 
lista, ambos son el nombre local que van a recibir estas variables.

-> Por un lado, tareaObj incrustará el texto en la posición que le corresponde en la lista. Por otro lado, index nos dará una
variable para poder manipular especificamente los objetos de la lista desde su posición. (Esto logrado gracias a los atributos
de forEach(), que sirven para manejar 1(elemento), 2(índice), 3(array). En este caso solo usamos los dos primeros)

->  Con btnFinish.setAttribute('onclick', `removeTask(${index})`); incrustamos el atributo de onclick a cada botón generado en 
las respectivas iteraciones. Gracias a haber capturado la posición en la lista usando la sintaxis de plantillas literales, 
es decir "(${})", pudimos incrustar la variable que declara la posición en la lista.

-> La función removeTask() rescata el index y opera "tareas.splice(index, 1)" para eliminar el objeto de la lista con el click
*/