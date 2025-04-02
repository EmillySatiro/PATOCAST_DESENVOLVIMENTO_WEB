/**
 * Obtém a porcentagem de progresso a partir do atributo "data-porcentagem" do elemento HTML.
 * Converte para um número decimal para ser usado na barra de progresso.
 */
const porcentagem = parseFloat(document.getElementById('progress-container').getAttribute('data-porcentagem')) / 100;

/**
 * Inicializa uma barra de progresso semicircular usando a biblioteca ProgressBar.js
 *
 * @type {ProgressBar.SemiCircle}
 */
var bar = new ProgressBar.SemiCircle("#progress-container", {
    strokeWidth: 6, // Espessura da linha de progresso
    color: '#252C4F', // Cor principal da barra
    trailColor: '#eee', // Cor de fundo da trilha da barra
    trailWidth: 1, // Espessura da trilha
    easing: 'easeInOut', // Tipo de animação
    duration: 1400, // Duração da animação em milissegundos
    svgStyle: null, // Estilos SVG
    text: {
        value: '', // Texto exibido dentro da barra (inicialmente vazio)
        alignToBottom: false // Alinhamento do texto
    },
    from: { color: '#252C4F' }, // Cor inicial da barra
    to: { color: '#252C4F' }, // Cor final da barra
    step: (state, bar) => {
        bar.path.setAttribute('stroke', state.color); // Define a cor da barra dinâmica
        
        // Define o valor percentual da barra com 2 casas decimais
        var value = (bar.value() * 100).toFixed(2); 
        if (value === "0.00") {
            bar.setText(''); // Se o valor for zero, não exibe texto
        } else {
            bar.setText(value + '%'); // Exibe o valor percentual
        }
        
        bar.text.style.color = state.color; // Define a cor do texto
    }
});

// Define a fonte e o tamanho do texto dentro da barra de progresso
bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
bar.text.style.fontSize = '2rem';

// Inicia a animação da barra de progresso até o valor calculado
bar.animate(porcentagem);
