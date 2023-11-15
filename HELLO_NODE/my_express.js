/*express : flask 같은 nodejs의 라이브러리*/
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello Express!')
})

app.get('/param', (req, res) => {
	var menu = req.query.menu
  	res.send('PARAM : ' + menu)
})

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : false }));
app.get('/post', (req, res) => {
  	res.send('POST : ')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})