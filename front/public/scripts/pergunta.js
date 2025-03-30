let indiceAtual = 0;
const perguntas = document.querySelectorAll(".respostas");
const progresso = document.querySelector(".progresso-indicador");

perguntas.forEach((_, index) => {
    let bolinha = document.createElement("div");
    bolinha.classList.add("bolinha");
    if (index === 0) bolinha.classList.add("ativa");
    progresso.appendChild(bolinha);
});

const bolinhas = document.querySelectorAll(".bolinha");

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

function avancar() {
    if (indiceAtual < perguntas.length - 1) {
        indiceAtual++;
        atualizarVisibilidade();
    }
}

function voltar() {
    if (indiceAtual > 0) {
        indiceAtual--;
        atualizarVisibilidade();
    }
}

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


function finalizandoForm(elemento){
    const idUser = getCookie("idUser");
    console.log("ID do usuário:",idUser);
    
    const respostas = document.querySelectorAll(".resposta input:checked");
    const valor = parseFloat(elemento.parentNode.querySelector("input").value);

    console.log("Valor:",valor);
    if (respostas.length < 2) {
        alert("Por favor, selecione todas as respostas antes de continuar.");
    }else{
        const respostasArray = Array.from(respostas).map((input, index) => ({
            pergunta: index + 1,
            resposta: input.value
        }));
    
        respostasArray.push({ pergunta: 3, resposta: valor });
    
        const respostasJson = JSON.stringify(respostasArray);
        const xhr = new XMLHttpRequest();
        
        console.log("Repostas:",respostasJson);
    
        xhr.open("POST", `http://127.0.0.1:5000/respostas/id=${idUser}`, true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                console.log("Respostas enviadas com sucesso!");
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

document.querySelectorAll(".resposta").forEach(div => {
    div.classList.remove("selecionado");
    div.querySelector("input").checked = false;
});

atualizarVisibilidade();