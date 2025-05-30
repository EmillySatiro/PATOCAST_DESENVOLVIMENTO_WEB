document.addEventListener('DOMContentLoaded', function() {
    var box = document.querySelector('.box-gasto-total');
    var container = document.getElementById('progress-container');
    if (box && container) {
        var porcentagem = parseFloat(container.getAttribute('data-porcentagem'));
        var styles = getComputedStyle(document.documentElement);
        var verde = styles.getPropertyValue('--verde');
        var amarelo = styles.getPropertyValue('--amarelo');
        var vermelho = styles.getPropertyValue('--vermelho');
        var cor;

        if (porcentagem < 50) {
            cor = verde;
        } else if (porcentagem < 100) {
            cor = amarelo;
        } else {
            cor = vermelho;
        }

        box.style.boxShadow = '10px 10px 2px ' + cor;
    }
});