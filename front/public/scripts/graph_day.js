function getCookie(nome) {
    let cookies = document.cookie.split("; ");
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].split("=");
        if (cookie[0] === nome) {
            return cookie[1];
        }
    }
    return null;
}

fetch('http://127.0.0.1:5000/transacao_days_in_month/id=' + getCookie("idUser"))
.then(response => response.json())
.then(data => {
    var meses = Object.keys(data);
    var compras = Object.values(data);

    var ctx = document.getElementById("meuGrafico");

    if (!ctx) {
        return;
    }

    new Chart(ctx.getContext("2d"), {
        type: "bar",
        data: {
            labels: meses,
            datasets: [{
                label: "Compras",
                data: compras,
                backgroundColor: "#eb8317",
                borderColor: "#eb8317",
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
})
.catch(error => console.error('Erro ao carregar dados:', error));