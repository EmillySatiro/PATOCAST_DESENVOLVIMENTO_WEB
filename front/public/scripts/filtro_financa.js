  /**
 * Função para buscar as transações com base nos filtros selecionados.
 * Envia uma requisição para a API e atualiza a tabela de transações.
 */
async function buscarTransacoes() {
  /** @type {string} */
  const mes = document.getElementById("mes").value; // Captura o valor do filtro de mês
  
  /** @type {string} */
  const categoria = document.getElementById("categoria").value; // Captura o valor do filtro de categoria
  
  /** @type {number} */
  const idUser = 1; // Defina ou pegue o ID do usuário (ajustar conforme necessário)

  // Monta a URL com os filtros
  let url = `http://localhost:5000/transacao/?id=${idUser}`;
  if (mes) url += `&mes=${mes}`;
  if (categoria) url += `&categoria=${categoria}`;

  try {
      // Envia a requisição para a API
      const response = await fetch(url);
      const data = await response.json();

      console.log(data); // Para depuração, remova em produção

      /** @type {HTMLElement} */
      const gasto_total = document.getElementById("gasto_total");
      
      // Calcula o total de gastos
      const total = data.reduce((acc, transacao) => acc + parseFloat(transacao.valor), 0);
      gasto_total.innerHTML = `R$${total.toFixed(2)}`; // Atualiza o total de gastos

      /** @type {HTMLTableElement} */
      const tabela = document.querySelector('.table-info');
      tabela.innerHTML = ""; // Limpa a tabela antes de preencher com os novos dados

      if (data.length) {
          data.forEach(transacao => {
              let row = tabela.insertRow();
              row.insertCell(0).textContent = transacao.estabelecimento;
              row.insertCell(1).textContent = transacao.categoria;
              row.insertCell(2).textContent = transacao.data;
              row.insertCell(3).textContent = `R$${transacao.valor}`;
          });
      }
  } catch (error) {
      console.error("Erro ao buscar transações:", error);
  }
}

// Evento de mudança para atualizar os dados quando o filtro for alterado
document.getElementById("mes").addEventListener("change", buscarTransacoes);
document.getElementById("categoria").addEventListener("change", buscarTransacoes);
