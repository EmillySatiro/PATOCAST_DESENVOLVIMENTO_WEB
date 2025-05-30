document.addEventListener('DOMContentLoaded', function() {
    const text = document.getElementById('text-limite');
    var valor = parseFloat(text.innerText.replace('R$', '').replace('.', '').replace(',', '.'));
    console.log(valor);
    if(valor < 0) {
        text.className += 'estourado';
    }
});