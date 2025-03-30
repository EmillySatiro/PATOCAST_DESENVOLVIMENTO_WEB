var bar = new ProgressBar.Circle("#progress-container", {
    strokeWidth: 6,
    color: '#000000',
    trailColor: '#eee',
    trailWidth: 1,
    easing: 'easeInOut',
    duration: 1400,
    svgStyle: null,
    text: {
        value: '',
        alignToBottom: false,
        color: '#000000',
    },
    from: {color: '#ff8225'},
    to: {color: '#ff8225'},
    step: (state, bar) => {
        bar.path.setAttribute('stroke', state.color);
        
        // Mostrar com 2 casas decimais
        var value = (bar.value() * 100).toFixed(0);  
        if (value === "0.00") {
            bar.setText('');
        } else {
            bar.setText(value + '%');
        }

        bar.text.style.color = '#000000'; 
    }
});

// Estilizando o texto
if (bar.text) {
    bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
    bar.text.style.fontSize = '2rem';
}

var progress = 0.0; // Valor inicial

bar.animate(progress); 