document.addEventListener("btnDownload", async (event) => {
  const idUser = 1; // Defina ou pegue o ID do usuário
  
  const mes = document.getElementById("mes").value;
  const categoria = document.getElementById("categoria").value;

  // Monta a URL com os filtros
  let url = `http://localhost:5000/transacao/?id=${idUser}`;
  if (mes && mes !== "todos") url += `&mes=${mes}`;
  if (categoria && mes !== "todas") url += `&categoria=${categoria}`;

  // Envia a requisição para a API
  const response = await fetch(url);
  const data = await response.json();

  console.log(data); // Para depuração, remova em produção

  const total = data.reduce((acc, transacao) => acc + parseFloat(transacao.valor), 0); // Calcula o total de gastos
  const gasto_total = document.getElementById("gasto_total");
  gasto_total.innerHTML = `R$${total.toFixed(2)}`; // Atualiza o total de gastos

  // Aqui você pode adicionar a lógica para gerar o PDF com os dados filtrados
});