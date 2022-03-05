var express = require("express");
const Pressure = require('../models/index').model("Pressure");
const Temperature = require('../models/index').model("Temperature");
var router = express.Router();

router.post('/', async function (req, res, next) {
  try {
    Pressure.destroy({ truncate: true, cascade: false })
    Temperature.destroy({ truncate: true, cascade: false })
    console.log('Limpando banco de dados.!');
    res.json({});
  } catch (e) {
    console.log(e);
    res.status(400).send(e);
  }
});
module.exports = router;