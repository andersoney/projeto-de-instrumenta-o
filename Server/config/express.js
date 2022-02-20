
const express = require('express')
const app = express()
const port = 8081
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use(require("../routes/index"))

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})
