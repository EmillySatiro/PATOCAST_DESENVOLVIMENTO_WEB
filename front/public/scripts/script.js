// Lista de imagens para o slideshow
const images = [
    "./images/slideshow/slideshow_1.png",
    "./images/slideshow/slideshow_2.png"
];

// Elementos do DOM usados no slideshow
const div_image = document.querySelector("div[name=slideshow]");
const image = document.getElementById("imagem-login-esquerda");
const points = document.getElementsByClassName("select-image");

// Índice inicial da imagem exibida
let index = 0;

/**
 * Função responsável por criar os indicadores (pontos) do slideshow.
 * Cada ponto permitirá selecionar manualmente uma imagem do slideshow.
 */
function slideShowOptions() {
    for (let i = 0; i < images.length; i++) {
        div_image.innerHTML += `<span class="select-image" onclick="selecionarImage(${i})"></span>`;
    }
}

/**
 * Atualiza a imagem do slideshow de acordo com o índice fornecido.
 * @param {number} n - Índice da imagem a ser exibida.
 */
function slideShowImage(n) {
    image.src = images[n];
    
    // Remove a classe "active" de todos os pontos
    for (let i = 0; i < images.length; i++) {
        points[i].className = points[i].className.replace(" active", "");
    }
    
    // Adiciona a classe "active" ao ponto correspondente à imagem atual
    points[n].className += " active";

    // Atualiza o índice atual
    index = n;
}

/**
 * Permite a seleção manual de uma imagem do slideshow através dos pontos indicadores.
 * @param {number} value - Índice da imagem selecionada.
 */
function selecionarImage(value) {
    slideShowImage(value);
}

/**
 * Alterna automaticamente entre as imagens do slideshow em intervalos de tempo.
 * A cada 15 segundos, a imagem exibida é alterada.
 */
function showSlides() {
    if (index >= images.length - 1) {
        index = 0;
    } else {
        index++;
    }
    
    slideShowImage(index);
    
    // Define o tempo de transição entre as imagens (15 segundos)
    setTimeout(showSlides, 15000);
}

/**
 * Alterna a visibilidade da senha no campo de entrada.
 * Se a senha estiver oculta (password), ela é exibida (text) e vice-versa.
 */
function mostrarSenha() {
    const input_senha = document.getElementById("senha");
    
    if (input_senha.type === "password") {
        input_senha.type = "text";
    } else {
        input_senha.type = "password";
    }
}

// Inicializa o slideshow
slideShowOptions();
showSlides();
