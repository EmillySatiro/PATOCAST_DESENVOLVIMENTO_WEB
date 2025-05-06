document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("myModal");
    const btn = document.getElementById("add");
    const span = document.querySelector(".close");

    btn.onclick = function () {
        modal.style.display = "block";
    }

    span.onclick = function () {
        modal.style.display = "none";
    }

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});