contador = 0;
let opcion;
do {
    opcion = prompt("Escoja una opción:\n1) sumar 1\n2) restar 1\n3) duplicar\n4) dividir\n5) salir\n Su contador actual es: " + contador);
    if (opcion == 1) {
        contador += 1;
    } else if (opcion == 2) {
        contador -= 1;
    } else if (opcion == 3) {
        contador *= 2;
    } else if (opcion == 4) {
        contador /= 2;
    } else if (opcion == 5 || opcion == null) {
        alert("adiós")
    } else {
        alert("opción inválida");
    }
} while (opcion != 5 && opcion !== null);