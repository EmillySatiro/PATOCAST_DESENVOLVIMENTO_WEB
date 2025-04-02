/**
 * Índice atual da pergunta sendo exibida.
 * @type {number}
 */
let indiceAtual = 0;

/**
 * Seleciona todas as perguntas e o indicador de progresso.
 */
const perguntas = document.querySelectorAll(".respostas");
const progresso = document.querySelector(".progresso-indicador");

/**
 * Cria indicadores visuais para cada pergunta.
 */
perguntas.forEach((_, index) => {
    let bolinha = document.createElement("div");
    bolinha.classList.add("bolinha");
    if (index === 0) bolinha.classList.add("ativa");
    progresso.appendChild(bolinha);
});

const bolinhas = document.querySelectorAll(".bolinha");

/**
 * Atualiza a visibilidade da pergunta atual e do indicador de progresso.
 */
function atualizarVisibilidade() {
    perguntas.forEach((pergunta, index) => {
        pergunta.classList.toggle("active", index === indiceAtual);
    });

    bolinhas.forEach((bolinha, index) => {
        bolinha.classList.toggle("ativa", index === indiceAtual);
    });

    document.getElementById("btn-voltar").disabled = indiceAtual === 0;
    document.getElementById("btn-avancar").disabled = indiceAtual >= perguntas.length - 1;
}

/**
 * Avança para a próxima pergunta.
 */
function avancar() {
    if (indiceAtual < perguntas.length - 1) {
        indiceAtual++;
        atualizarVisibilidade();
    }
}

/**
 * Retorna para a pergunta anterior.
 */
function voltar() {
    if (indiceAtual > 0) {
        indiceAtual--;
        atualizarVisibilidade();
    }
}

/**
 * Seleciona uma resposta e atualiza a barra de progresso.
 * @param {HTMLElement} elemento - Elemento da resposta selecionada.
 */
function selecionar(elemento) {
    const parent = elemento.parentNode;
    const alreadySelected = parent.querySelector(".selecionado");

    if (!alreadySelected) {
        console.log("Elemento não selecionado:", elemento);
        progress += 1 / perguntas.length;
        bar.animate(progress);
    }

    parent.querySelectorAll(".resposta").forEach(div => {
        div.classList.remove("selecionado");
        div.querySelector("input").checked = false;
    });

    elemento.classList.add("selecionado");
    elemento.querySelector("input").checked = true;
}

/**
 * Obtém um cookie pelo nome.
 * @param {string} nome - Nome do cookie.
 * @returns {string|null} Valor do cookie ou null se não encontrado.
 */
function getCookie(nome) {
    let cookies = document.cookie.split("; ");
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].split("=");
        if (cookie[0] === nome) {
            return cookie[1];
        }
    }
    return null;
}

/**
 * Finaliza o formulário e envia as respostas ao servidor.
 * @param {HTMLElement} elemento - Elemento do botão de envio.
 */
function finalizandoForm(elemento) {
    const idUser = getCookie("idUser");
    console.log("ID do usuário:", idUser);
    
    const respostas = document.querySelectorAll(".resposta input:checked");
    const valor = parseFloat(elemento.parentNode.querySelector("input").value);
    console.log("Valor:", valor);
    
    if (respostas.length < 2) {
        alert("Por favor, selecione todas as respostas antes de continuar.");
    } else {
        const respostasArray = Array.from(respostas).map((input, index) => ({
            pergunta: index + 1,
            resposta: input.value
        }));
    
        respostasArray.push({ pergunta: 3, resposta: valor });
        
        const respostasJson = JSON.stringify(respostasArray);
        const xhr = new XMLHttpRequest();
        
        console.log("Respostas:", respostasJson);
    
        xhr.open("POST", `http://127.0.0.1:5000/respostas/id=${idUser}`, true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                window.location.href = "/inicio";
            } else if (xhr.readyState === 4) {
                console.error("Erro ao enviar respostas:", xhr.statusText);
            }
        };
        
        setTimeout(() => {
            console.log("Enviando respostas...");
        }, 1000);
        
        xhr.send(respostasJson);
    
        progress = (indiceAtual + 1) / perguntas.length;
        bar.animate(progress); 
    }
}

// Limpa a seleção inicial de respostas
/**
 * Remove a seleção inicial de todas as respostas.
 */
document.querySelectorAll(".resposta").forEach(div => {
    div.classList.remove("selecionado");
    div.querySelector("input").checked = false;
});

// Inicializa a visibilidade da primeira pergunta
atualizarVisibilidade();