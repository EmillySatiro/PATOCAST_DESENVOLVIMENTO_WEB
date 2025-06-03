const lista = document.getElementById("nav-options")

lista.addEventListener("click",
    (e) => {
        // if(e.detail)
        if(!(e.detail)){
            if(e.target.className != "active"){
                for (let i = 0; i < lista.children.length; i++) {
                    lista.children[i].className = lista.children[i].className.replace("active");
                }
                e.target.className = "active";
            }
        }
    }
)

function verificaPage(){
    const url = window.location.pathname;

    if(url == "/inicio"){
        lista.children[0].className = "active"
    }else if(url == "/contas"){
        lista.children[1].className = "active"
    }else if(url == "/metas"){
        lista.children[2].className = "active"
    }else if(url == "/financas"){
        lista.children[3].className = "active"
    }else if(url == "/historico"){
        lista.children[4].className = "active"
    }else if(url == "/ajuda"){
        lista.children[5].className = "active"
    }else if(url == "/perfil"){
        lista.children[6].className = "active"
    }
}

verificaPage()

function verificaNav(){
    const nav = document.getElementById("list-nav")
    const navigation = document.getElementById("navigation-bar")

    if(navigation.className.search(" occult") < 0){
        nav.src = './assets/list_preto.svg'
        navigation.className += " occult"
    }else{
        nav.src = './assets/list_branco.svg'
        navigation.className = navigation.className.split(" occult")[0]
    }
    // nav.className = "occullt"
}

const profile = document.getElementById("profile-bar")

profile.addEventListener("click",ativaNavigation)

function ativaNavigation(){
    const navigation = document.getElementById("navigation-bar")

    if(navigation.className.search(" activate") < 0){
        navigation.className += " activate"
    }else{
        navigation.className = navigation.className.split(" activate")[0]
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// Atualiza o nome do usuário na tela
let username = getCookie("username"); 
if (username) {
    username = username.replace(/"/g, "");
    const usernameElements = document.querySelectorAll("#username");
    usernameElements.forEach(element => {
        element.textContent = username;
    });
}

function fecharModal(){
    const modal = document.querySelector(".modal");
    if (modal) {
        modal.style.display = "none";

        const currentUrl = window.location.href.split("?")[0];
        console.log("Current URL:", currentUrl);
        if (currentUrl.endsWith("/cadastrar")) {
            console.log("Redirecting to /perguntas");
            window.location.href = "/perguntas";
        } else if (currentUrl.endsWith("/alterar-senha")) {
            window.location.href = "/";
        }
    }
}