/**
 * Aguarda o carregamento completo do DOM antes de executar o script.
 */
document.addEventListener('DOMContentLoaded', function() {
  /** @type {HTMLSelectElement} */
  const mesSelect = document.getElementById('mes'); // Seleciona o elemento <select> para o mês
  
  /** @type {HTMLSelectElement} */
  const categoriaSelect = document.getElementById('categoria'); // Seleciona o elemento <select> para a categoria
  
  /** @type {HTMLAnchorElement} */
  const downloadLink = document.getElementById('downloadLink'); // Seleciona o link de download
  
  /** @type {string} */
  const idUser = getCookie('idUser'); // Obtém o ID do usuário a partir dos cookies
  
  /**
   * Atualiza o link de download do PDF com os parâmetros selecionados.
   */
  function updateDownloadLink() {
      const mes = mesSelect.value;
      const categoria = categoriaSelect.value;
      downloadLink.href = `/exportar-pdf/?id=${idUser}&mes=${mes}&categoria=${categoria}`;
  }
  
  // Adiciona eventos de mudança nos selects para atualizar o link de download
  mesSelect.addEventListener('change', updateDownloadLink);
  categoriaSelect.addEventListener('change', updateDownloadLink);
  
  // Atualiza o link de download inicialmente
  updateDownloadLink();
});
