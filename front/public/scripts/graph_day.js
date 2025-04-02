/**
 * Função para obter o valor de um cookie específico.
 * @param {string} nome - Nome do cookie a ser buscado.
 * @returns {string|null} - Valor do cookie ou null se não encontrado.
 */

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

/**
 * Faz uma requisição para obter os dados de transações por mês e exibe em um gráfico de barras.
 */
fetch('http://127.0.0.1:5000/transacao_days_in_month/id=' + getCookie("idUser"))
    .then(response => response.json())
    .then(data => {
        /** @type {string[]} */
        var meses = Object.keys(data); // Obtém os meses das transações
        
        /** @type {number[]} */
        var compras = Object.values(data); // Obtém os valores das transações
        
        /** @type {HTMLCanvasElement} */
        var ctx = document.getElementById("meuGrafico");

        if (!ctx) {
            return;
        }

        // Criação do gráfico de barras usando Chart.js
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