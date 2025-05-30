async function buscarTransacoes() {
  // Captura os valores dos filtros
  const mes = document.getElementById("mes").value;
  const categoria = document.getElementById("categoria").value;
  const idUser = getCookie("idUser"); // Obtém o ID do usuário do cookie

  // Monta a URL com os filtros
  let url = `http://localhost:5000/transacao/?id=${idUser}`;
  if (mes) url += `&mes=${mes}`;
  if (categoria) url += `&categoria=${categoria}`;

  // Envia a requisição para a API
  const response = await fetch(url);
  const data = await response.json();

  console.log(data); // Para depuração, remova em produção

  const gasto_total = document.getElementById("gasto_total");
  const total = data.reduce((acc, transacao) => acc + parseFloat(transacao.valor), 0); // Calcula o total de gastos
  gasto_total.innerHTML = `R$${total.toFixed(2)}`.replace('.', ','); // Atualiza o total de gastos

  // Atualiza a tabela com as transações filtradas
  const tabela = document.querySelector('.table-info');
  tabela.innerHTML = "";

  if (data.length) {
      data.forEach(transacao => {
          let row = tabela.insertRow();
          row.insertCell(0).textContent = transacao.estabelecimento;
          row.insertCell(1).textContent = transacao.categoria;
          row.insertCell(2).textContent = transacao.data;
          row.insertCell(3).textContent = `R$${transacao.valor}`.replace('.', ',');
      });
  }

  // Atualiza o gráfico com os novos dados
  atualizarGrafico(data);
}

buscarTransacoes();

document.getElementById("mes").addEventListener("change", buscarTransacoes);
document.getElementById("categoria").addEventListener("change", buscarTransacoes);