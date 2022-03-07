var express = require("express");
const Pressure = require('../models/index').model("Pressure");
var router = express.Router();
router.get('/', async function (req, res, next) {
  try {
    let count = await Pressure.count();
    res.json(await Pressure.findAll({
      limit: 100, offset: count - 100
    }));
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/types', async function (req, res, next) {
  try {
    const pressures = await Pressure.findAll({ attributes: ['type'], limit: 100, order: [['id', 'DESC']], group: 'type' })
    res.json(pressures.reverse());
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/bytype/:type', async function (req, res, next) {
  try {
    const pressures = await Pressure.findAll({ limit: 100, order: [['id', 'DESC']], where: { type: req.params.type } })
    res.json(pressures.reverse());
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/:id', async function (req, res, next) {
  try {
    const jane = await Pressure.findOne({ where: { id: req.params.id } })
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});

router.post('/', async function (req, res, next) {
  try {
    let pressure = req.body;
    console.log('Salvando Pressão!: ' + JSON.stringify(pressure));
    const jane = Pressure.build(pressure);
    await jane.save();
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});
router.put('/:id', async function (req, res, next) {
  try {
    let temp = req.body;
    console.log(req.params.id)
    const jane = await Pressure.findOne({ where: { id: req.params.id } });
    await jane.update(temp);
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});
router.delete('/:id', async function (req, res, next) {
  try {
    const jane = await Pressure.findOne({ where: { id: req.params.id } })
    await jane.destroy();
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});
module.exports = router;