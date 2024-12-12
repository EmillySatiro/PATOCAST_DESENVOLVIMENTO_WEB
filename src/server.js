const express = require('express')
const server = express()
const port = 3002

server.use(express.static("public"))
server.use(express.urlencoded({extended: true}))

const nunjucks = require('nunjucks')
nunjucks.configure(
  "src/views",{
    express: server,
    noCache: true
  }
)

// server.get('/images/valor', async (req, res) => {
//   image_list = await images('./public/images/slideshow')
//   res.json({ valor: image_list }); // Retorna o valor como JSON
// });

server.get('/login', async (req,res) => {
    return res.render('./auth/login.htm')
})

server.get('/cadastrar', async (req,res) => {
  return res.render('./auth/cadastrar.htm')
})

server.get('/recuperar_conta', async (req,res) => {
  return res.render('./auth/esqueci-senha.htm')
})

server.get('/inicio', async (req,res) => {
  return res.render('./navigation/inicio.htm')
})

server.get('/contas', async (req,res) => {
  return res.render('./navigation/contas.htm')
})

server.get('/metas', async (req,res) => {
  return res.render('./navigation/metas.htm')
})

server.get('/financas', async (req,res) => {
  return res.render('./navigation/financas.htm')
})

server.get('/ajuda', async (req,res) => {
  return res.render('./navigation/ajuda.htm')
})

server.get('/perfil', async (req,res) => {
  return res.render('./navigation/perfil.htm')
})

server.get('/historico', async (req,res) => {
  return res.render('./navigation/operacoes.htm')
})

server.listen(port)