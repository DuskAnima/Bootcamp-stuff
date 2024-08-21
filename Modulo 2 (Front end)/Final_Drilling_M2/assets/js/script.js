document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    alert("Formulario enviado. ¡Gracias por contactarme!");
});

$(document).ready(function() {
    const token = 'iU9YZIaWMJ3yvA27Ng5SGmlC';
    const teamId = 'animas-projects-e0066ff5'; 
    const url = `https://api.vercel.com/v13/deployments/prj_ho13BnkHk2LU212Y5hQ7OZJATCfQ
    ${teamId ? `?teamId=${teamId}` : ''}`;

    $.get(url, function(data) {
        const deployments = data.deployments;
        const list = $('#deployment-list');
        deployments.forEach(deployment => {
            const listItem = $('<li>').text(`Deployment: ${deployment.name} - ${deployment.url}`);
            list.append(listItem);
        });
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
        console.error('Error fetching deployments:', textStatus, errorThrown);
    });
});

//Vercel: iU9YZIaWMJ3yvA27Ng5SGmlC