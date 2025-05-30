document.addEventListener('DOMContentLoaded', function() {
    function atualizarBoxShadowMeta() {
        var boxGastoTotal = document.querySelector('.box-gasto-total');
        var boxGasto = document.querySelector('.box-gasto');
        var container = document.getElementById('progress-container');
        
        if (!container) return;
        
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
        
        if (window.innerWidth <= 720) {
            if (boxGastoTotal) boxGastoTotal.style.boxShadow = '5px 5px 2px ' + cor;
            if (boxGasto) boxGasto.style.boxShadow = 'none';
        } else {
            if (boxGastoTotal) boxGastoTotal.style.boxShadow = 'none';
            if (boxGasto) boxGasto.style.boxShadow = '10px 10px 2px ' + cor;
        }
    }

    atualizarBoxShadowMeta();

    window.addEventListener('resize', function() {
        atualizarBoxShadowMeta();
    });
});