/**
 * Adiciona um evento de clique à lista de navegação para alterar a classe ativa.
 */
const lista = document.getElementById("nav-options");
lista.addEventListener("click", (e) => {
    if (!(e.detail)) {
        if (e.target.className !== "active") {
            for (let i = 0; i < lista.children.length; i++) {
                lista.children[i].classList.remove("active");
            }
            e.target.classList.add("active");
        }
    }
});

/**
 * Verifica a URL atual e adiciona a classe "active" à opção de navegação correspondente.
 */
function verificaPage() {
    const url = window.location.pathname;
    const pages = ["/inicio", "/contas", "/metas", "/financas", "/historico", "/ajuda", "/perfil"];
    pages.forEach((page, index) => {
        if (url === page) {
            lista.children[index].classList.add("active");
        }
    });
}
verificaPage();

/**
 * Alterna a visibilidade da barra de navegação.
 */
function verificaNav() {
    const nav = document.getElementById("list-nav");
    const navigation = document.getElementById("navigation-bar");
    
    if (navigation.classList.contains("occult")) {
        nav.src = './assets/list_branco.svg';
        navigation.classList.remove("occult");
    } else {
        nav.src = './assets/list_preto.svg';
        navigation.classList.add("occult");
    }
}

/**
 * Ativa ou desativa a navegação lateral ao clicar no perfil.
 */
const profile = document.getElementById("profile-bar");
profile.addEventListener("click", ativaNavigation);

function ativaNavigation() {
    const navigation = document.getElementById("navigation-bar");
    navigation.classList.toggle("activate");
}

/**
 * Obtém o valor de um cookie pelo nome.
 * @param {string} name - Nome do cookie.
 * @returns {string|null} Valor do cookie ou null se não encontrado.
 */
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts.pop().split(';').shift() : null;
}

// Atualiza o nome do usuário na tela
let username = getCookie("username");
if (username) {
    username = username.replace(/"/g, "");
    document.getElementById("username").textContent = username;
}

/**
 * Fecha o modal e redireciona para a URL apropriada.
 */
function fecharModal() {
    const modal = document.querySelector(".modal");
    if (modal) {
        modal.style.display = "none";

        const currentUrl = window.location.href.split("?")[0];
        window.location.href = currentUrl;

        if (currentUrl.endsWith("/cadastrar")) {
            console.log("Redirecting to /perguntas");
            window.location.href = "/perguntas";
        }
    }
}
