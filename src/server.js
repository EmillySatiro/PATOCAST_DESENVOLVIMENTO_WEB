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

server.get('/', (req,res) => {
    return res.render('home.htm')
})

server.listen(port)