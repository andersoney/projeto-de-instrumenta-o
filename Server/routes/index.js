var express = require("express");
var router = express.Router();
var temperature=require("./temperature")
var pressure=require("./pressure")
router.use("/temperature",temperature);
router.use("/pressure",pressure);

module.exports = router;