document.addEventListener('DOMContentLoaded', function() {
  const mesSelect = document.getElementById('mes');
  const categoriaSelect = document.getElementById('categoria');
  const downloadLink = document.getElementById('downloadLink');
  const idUser = getCookie('idUser');
  
  function updateDownloadLink() {
      const mes = mesSelect.value;
      const categoria = categoriaSelect.value;
      downloadLink.href = `/exportar-pdf/?id=${idUser}&mes=${mes}&categoria=${categoria}`;
  }
  
  mesSelect.addEventListener('change', updateDownloadLink);
  categoriaSelect.addEventListener('change', updateDownloadLink);
  updateDownloadLink();
});