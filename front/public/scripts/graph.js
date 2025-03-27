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

fetch('http://127.0.0.1:5000/transacao_mes/id=' + getCookie("idUser"))
.then(response => response.json())
.then(data => {
    console.log("Dados recebidos:", data);
    console.log("Meses:", Object.keys(data));
    console.log("Vendas:", Object.values(data));
    print(data);
    var meses = Object.keys(data);
    var vendas = Object.values(data);

    var ctx = document.getElementById("meuGrafico");
    console.log(ctx);
    if (!ctx) {
        console.error("Elemento #meuGrafico não encontrado!");
        return;
    }

    new Chart(ctx.getContext("2d"), {
        type: "bar",
        data: {
            labels: meses,
            datasets: [{
                label: "Vendas",
                data: vendas,
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
