const porcentagem = parseFloat(document.getElementById('progress-container').getAttribute('data-porcentagem')) / 100;

var bar = new ProgressBar.SemiCircle("#progress-container", {
    strokeWidth: 6,
    color: '#252C4F',
    trailColor: '#eee',
    trailWidth: 1,
    easing: 'easeInOut',
    duration: 1400,
    svgStyle: null,
    text: {
        value: '',
        alignToBottom: false
    },
    from: {color: '#252C4F'},
    to: {color: '#252C4F'},
    step: (state, bar) => {
        bar.path.setAttribute('stroke', state.color);
        
        // Mostrar com 2 casas decimais
        var value = (bar.value() * 100).toFixed(2);  // Com 2 casas decimais
        if (value === "0.00") {
            bar.setText('');
        } else {
            bar.setText(value + '%');
        }

        bar.text.style.color = state.color;
    }
});

bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
bar.text.style.fontSize = '2rem';

bar.animate(porcentagem); 