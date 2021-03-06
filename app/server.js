const express = require('express')
const axios = require('axios')
const app = express()

app.use(express.static('public'))

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html')
})

app.get('/vault_creds', (req, res) => {
  axios.post('http://vault:8200/v1/auth/userpass/login/app', {
      password: 'app'
    })
    .then(response => {
      console.log(response.body)
      res.sendStatus(response.statusCode)
    })
    .catch(error => {
      console.log(error)
      res.sendStatus(500)
    })
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