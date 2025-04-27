let meuGrafico; // Variável global para armazenar a instância do gráfico

// Função para atualizar o gráfico
function atualizarGrafico(data) {
    const categorias = [...new Set(data.map(transacao => transacao.categoria))]; // Obtém categorias únicas
    const valores = categorias.map(categoria => {
        return data
            .filter(transacao => transacao.categoria === categoria)
            .reduce((acc, transacao) => acc + parseFloat(transacao.valor), 0);
    });

    const ctx = document.getElementById("meuGrafico");

    if (!ctx) {
        return;
    }

    // Destroi o gráfico anterior, se existir
    if (meuGrafico) {
        meuGrafico.destroy();
    }

    // Cria um novo gráfico
    meuGrafico = new Chart(ctx.getContext("2d"), {
        type: "bar",
        data: {
            labels: categorias,
            datasets: [{
                label: "Gastos por Categoria",
                data: valores,
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
}