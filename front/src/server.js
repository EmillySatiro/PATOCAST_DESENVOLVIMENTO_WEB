const express = require('express')
const cookieParser = require('cookie-parser');

const server = express()
const port = process.env.PORT || 3000
const host_backend = process.env.HOST_BACKEND || 'localhost'
const port_backend = process.env.PORT_BACKEND || 5000

console.log(`Frontend rodando na porta ${port}`)
console.log(`Backend rodando na porta ${port_backend}`)
console.log(`Host do backend: ${host_backend}`)

server.use(express.static("public"))
server.use(express.urlencoded({extended: true}))
server.use(cookieParser())

const nunjucks = require('nunjucks')
nunjucks.configure(
  "src/views",{
    express: server,
    noCache: true,
    autoescape: true
  }
)

server.get('/', async (req,res) => {
    return res.render('./auth/login.htm')
})

server.get('/cadastrar', async (req,res) => {
  return res.render('./auth/cadastrar.htm')
})

server.get('/recuperar_conta', async (req,res) => {
  return res.render('./auth/esqueci-senha.htm')
})

server.get('/inicio', async (req,res) => {
  let idUser = req.cookies.idUser

  const response = await fetch(
    `http://${host_backend}:${port_backend}/transacao?id=${idUser}`
  );

  const response_user = await fetch(
    `http://${host_backend}:${port_backend}/users/id=${idUser}`
  );

  const response_cartao = await fetch(
    `http://${host_backend}:${port_backend}/cards/id=${idUser}`
  );

  dados = await response.json()
  const user_data = await response_user.json()
  const cartao_data = await response_cartao.json()
  
  gasto = parseFloat(dados.reduce((acc, curr) => acc + parseFloat(curr.valor), 0)).toFixed(2)
  porcentagem = (gasto / user_data.limite) * 100;
  
  return res.render('./navigation/inicio.htm', {
    transacoes: dados,
    gasto_total: gasto,
    limite: parseFloat(user_data.limite) - gasto,
    porcentagem: porcentagem > 100 ? 100 : porcentagem,
    quantidade_cartao: cartao_data.length,
    cartoes: cartao_data,
  })
})

server.get('/contas', async (req,res) => {

  const response = await fetch(
    `http://${host_backend}:${port_backend}/cards/id=${req.cookies.idUser}`
  );

  const cartoes = await response.json()
  
  console.log(cartoes)

  return res.render('./navigation/contas.htm', {
    idUser: req.cookies.idUser,
    cartoes: cartoes
  })
})

server.get('/metas', async (req,res) => {
  let idUser = req.cookies.idUser
  
  const user = await fetch(
    `http://${host_backend}:${port_backend}/users/id=${idUser}`
  );

  const response = await fetch(
    `http://${host_backend}:${port_backend}/transacao_categoria/id=${idUser}`
  );
  
  dados = await response.json()
  
  const user_data = await user.json()
  gasto = Object.values(dados).reduce((acc, categoria) => acc + categoria.total_gasto, 0);

  porcentagem = (gasto / user_data.limite) * 100;

  return res.render('./navigation/metas.htm', {
    categorias: dados,
    limite: user_data.limite,
    gasto_limite: user_data.limite - gasto,
    gasto_total: gasto,
    porcentagem: porcentagem > 100 ? 100 : porcentagem,
  })
})

server.get('/financas', async (req,res) => {
  let idUser = req.cookies.idUser

  const response_transacao = await fetch(
    `http://${host_backend}:${port_backend}/transacao?id=${idUser}`
  );
  dados = await response_transacao.json()

  const response_pendente = await fetch(
    `http://${host_backend}:${port_backend}/transacao_next_transactions/id=${idUser}`
  );
  gasto_pendente = await response_pendente.json()

  const response_categorias = await fetch(
    `http://${host_backend}:${port_backend}/get_categorias/id=${idUser}`
  );
  categorias = await response_categorias.json()

  const response_meses = await fetch(
    `http://${host_backend}:${port_backend}/transacao_mes/id=${idUser}`
  );
  meses = await response_meses.json()

  return res.render('./navigation/financas.htm', {
    transacoes: dados,
    gasto_total: parseFloat(dados.reduce((acc, curr) => acc + parseFloat(curr.valor), 0)).toFixed(2),
    pendente: parseFloat(gasto_pendente.pendente).toFixed(2),
    categorias: categorias,
    meses: meses,
  })
})

server.get('/ajuda', async (req,res) => {
  return res.render('./navigation/ajuda.htm')
})

server.get('/ajuda_selecionado', async (req,res) => {
  return res.render('./navigation/ajuda_selecionado.htm')
})

server.get('/perfil', async (req,res) => {
  let username = req.cookies.username
  let idUser = req.cookies.idUser

  return res.render('./navigation/perfil.htm', 
    {
      nome: username,
      idUser: idUser
    }
  )
})

server.get('/historico', async (req,res) => {
  let idUser = req.cookies.idUser

  const response = await fetch(
    `http://${host_backend}:${port_backend}/transacao?id=${idUser}`
  );
  dados = await response.json()
  return res.render('./navigation/operacoes.htm',{transacoes: dados})
})

server.get('/perguntas', async (req,res) => {
  return res.render('./auth/perguntas.htm')
})

server.get('/relatorio', async (req,res) => {
  return res.sendFile('./pdf/relatorio.htm', {
    nome: 'Jonas César'
  })

})

server.listen(port)