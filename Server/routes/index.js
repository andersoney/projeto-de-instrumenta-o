var express = require("express");
var router = express.Router();
var temperature = require("./temperature")
var pressure = require("./pressure")
var clean = require("./clean")
router.use("/temperature", temperature);
router.use("/pressure", pressure);
router.use("/clean", clean);

module.exports = router;