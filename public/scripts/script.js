const images = [
    "./images/slideshow/slideshow_1.png",
    "./images/slideshow/slideshow_2.png"
]
const div_image = document.querySelector("div[name=slideshow]");
const image = document.getElementById("imagem-login-esquerda");
const points = document.getElementsByClassName("select-image");

let index = 0

function slideShowOptions(){
    for (let i = 0; i < images.length; i++) {
        div_image.innerHTML += `<span class="select-image" onclick="selecionarImage(${i})"></span>`
    }
}

function slideShowImage(n){
    
    image.src = images[n];
    
    for (let i = 0; i < images.length; i++) {
        points[i].className = points[i].className.replace(" active", "");
    }
    points[n].className += " active";

    index = n;
}

function selecionarImage(value){
    slideShowImage(value);
}

function showSlides() {
    if(index >= images.length - 1) { 
        index = 0
    }else{
        index++;
    }
    
    slideShowImage(index);
    
    setTimeout(showSlides, 15000); // Change image every 2 seconds
}

function mostrarSenha(){
    const input_senha = document.getElementById("senha")
    
    if(input_senha.type == "password")
        input_senha.type = "text";
    else
        input_senha.type = "password";
}

slideShowOptions();
showSlides();