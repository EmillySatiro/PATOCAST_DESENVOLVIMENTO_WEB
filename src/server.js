const express = require('express')
const server = express()
const port = 3000

const images = require('./scripts/images')

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

server.get('/', async (req,res) => {
    image_list = await images('./public/images/slideshow')
    return res.render('home.htm', {
      images: image_list
    })
})

server.listen(port)