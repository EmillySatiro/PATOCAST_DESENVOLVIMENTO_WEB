const fs = require('node:fs').promises;

async function listarArquivosDoDiretorio(diretorio, arquivos) {
    
    if(!arquivos)
        arquivos = [];
    
    let listaDeArquivos = await fs.readdir(diretorio);

    return listaDeArquivos;
}

module.exports = listarArquivosDoDiretorio