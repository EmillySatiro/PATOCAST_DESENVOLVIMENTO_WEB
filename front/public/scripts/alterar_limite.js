const text_limite_alterar = document.getElementById("text-limite-alterar");
const myModal = document.getElementById("myModal");
const closeBtn = document.querySelector("#myModal .close");

if (text_limite_alterar) {
    text_limite_alterar.addEventListener("click", function () {
        if (myModal) {
            myModal.style.display = "block";
        }
    });
}

if (closeBtn) {
    closeBtn.addEventListener("click", function () {
        myModal.style.display = "none";
    });
}

// Fecha o modal ao clicar fora dele
window.addEventListener("click", function(event) {
    if (event.target === myModal) {
        myModal.style.display = "none";
    }
});