let opcion = prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesides.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas")
const error = "La opción ingresada no es válida. Gracias por preferir nuestros servicios"
//Opción 1


if (opcion == 1) {
    let op = prompt("Seleccione una opción:\n 1.-Ver Boleta\n2.-Pagar cuenta");
    if (op == 1) {
        alert("Haga click aquí para descargar su boleta.");
    } else if (op == 2) {
        alert("Usted está siendo transferido. Espere, por favor...");
    } else {
        alert(error);
    }

} else if (opcion == 2) {
    let op = prompt("Seleccione una opción:\n1.-Problemas con la señal\n2.-Problemas con llamadas");
    if (op == 1 || op == 2) {
        let solicitud = prompt("A continuación secriba su solicitud:");
        alert("Estimado usuario, su solicitud: " + "'" + solicitud + "'" + " Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.");
    }
    else {
        alert(error);
    }
} else if (opcion == 3) {
    let oferta = prompt("¡Mentel tiene una oferta comercial acorde a tus necesidades!\nPara conocer más información y ser asesorado personalmente por un ejecutivo escribe 'SI' y un ejecutivo te llamará. De lo contrario ingrese 'NO'")
    if (oferta == "SI" || oferta == "si" || oferta == "Si"){
        alert("Un ejecutivo contactará con usted.");
    }
    else {
        alert("Gracias por preferir nuestros servicios.")
    }
} else if (opcion == 4) {
    let consulta = prompt("A continuación escriba su consulta")
    alert("Estimado usuario, su consulta: " + "'" + consulta + "'" + " Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.")
} else {
    alert(error)
}

