const express = require('express')
const server = express()
const port = 3000

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
    return res.render('login.htm')
})

server.get('/cadastrar', async (req,res) => {
  return res.render('cadastrar.htm')
})

server.get('/recuperar_conta', async (req,res) => {
  return res.render('esqueci-senha.htm')
})

server.listen(port)