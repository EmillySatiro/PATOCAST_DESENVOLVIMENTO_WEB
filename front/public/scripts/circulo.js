/**
 * Inicializa um ProgressBar.Circle dentro do elemento com ID 'progress-container'.
 * A barra de progresso é animada e exibe um valor percentual.
 *
 * @requires ProgressBar.js
 */
var bar = new ProgressBar.Circle("#progress-container", {
    strokeWidth: 6, // Largura da linha de progresso
    color: '#000000', // Cor do progresso
    trailColor: '#eee', // Cor da trilha (fundo da barra)
    trailWidth: 1, // Largura da trilha
    easing: 'easeInOut', // Tipo de animação
    duration: 1400, // Duração da animação em milissegundos
    svgStyle: null, // Estilo SVG personalizado (null para padrão)
    text: {
        value: '', // Valor inicial do texto
        alignToBottom: false, // Alinhamento do texto
        color: '#000000', // Cor do texto
    },
    from: {color: '#ff8225'}, // Cor inicial da barra de progresso
    to: {color: '#ff8225'}, // Cor final da barra de progresso
    
    /**
     * Define o comportamento da barra em cada etapa da animação.
     * @param {Object} state - Estado da animação.
     * @param {Object} bar - Instância do ProgressBar.
     */
    step: (state, bar) => {
        bar.path.setAttribute('stroke', state.color);
        
        // Mostrar valor formatado em percentual
        var value = (bar.value() * 100).toFixed(0);  
        if (value === "0.00") {
            bar.setText('');
        } else {
            bar.setText(value + '%');
        }
        
        // Definir a cor do texto
        bar.text.style.color = '#000000'; 
    }
});

// Estilizando o texto dentro da barra de progresso
if (bar.text) {
    bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
    bar.text.style.fontSize = '2rem';
}

/**
 * Define o valor inicial da barra de progresso.
 * @type {number}
 */
var progress = 0.0; // Valor inicial

// Anima a barra até o valor especificado
bar.animate(progress);
