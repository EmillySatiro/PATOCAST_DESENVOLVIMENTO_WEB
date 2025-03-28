document.getElementById("btnDownload").addEventListener("click", () => {
    const { jsPDF } = window.jspdf; // Pegando jsPDF da janela global

    const doc = new jsPDF();
    doc.text("Relatório Financeiro", 20, 20);
    doc.text("Gasto Total: R$ 1500,00", 20, 40);
    doc.text("Limite Restante: R$ 500,00", 20, 60);

    doc.save("relatorio.pdf");
});
