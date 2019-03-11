<template>
  <div id="app">
    <button v-on:click="getCredentials" v-bind:style="{ background: credentialsButtonColor }">GET CREDENTIALS</button>
    <button v-on:click="readDatabase" v-bind:style="{ background: databaseReadButtonColor }">READ DATABASE</button>
    <button v-on:click="writeOnDatabase" v-bind:style="{ background: databaseWriteButtonColor }">WRITE ON DATABASE</button>
  </div>
</template>

<script>
import axios from 'axios'

const colors = {
  gray: '#353b48',
  green: '#4cd137',
  red: '#e84118'
}

export default {
  name: 'app',
  data () {
    return {
      credentialsButtonColor: colors.gray,
      databaseReadButtonColor: colors.gray,
      databaseWriteButtonColor: colors.gray,

    }
  },
  methods: {
    getCredentials () {
      axios.get('/vault_creds')
        .then(() => {
          this.credentialsButtonColor = colors.green
        })
        .catch(() => {
          this.credentialsButtonColor = colors.red
        })
    },
    readDatabase () {
      axios.get('/db_read')
        .then(() => {
          this.databaseReadButtonColor = colors.green
        })
        .catch(() => {
          this.databaseReadButtonColor = colors.red
        })
    },
    writeOnDatabase() {
      axios.post('/db_write', {})
        .then(() => {
          this.databaseWriteButtonColor = colors.green
        })
        .catch(() => {
          this.databaseWriteButtonColor = colors.red
        })
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  height: 100vh;
  justify-content: center;
  align-items: center;
}

button {
  font-family: 'Open Sans', sans-serif;
  font-size: 36px;
  color: white;
  width: 33.33%;
  height: 100%;
  outline: 0;
  cursor: pointer;
  margin: 0;
  border: 0;
}

button:hover {
  font-weight: bolder;
  opacity: 0.9;
}
</style>
