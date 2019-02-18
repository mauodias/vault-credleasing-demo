const express = require('express')
const app = express()

app.use(express.static('public'))

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html')
})

app.get('/vault_creds', (req, res) => {
  res.sendStatus(200)
})

app.get('/db_read', (req, res) => {
  res.sendStatus(200)
})

app.get('/db_write', (req, res) => {
  res.sendStatus(401)
})

app.listen(1234, () => {
  console.log('running')
})