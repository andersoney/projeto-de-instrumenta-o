var express = require("express");
const Temperature = require('../models/index').model("Temperature");
const Sequelize = require('sequelize');
const Op = Sequelize.Op;
var router = express.Router();
router.get('/', async function (req, res, next) {
  try {
    let count = await Temperature.count();
    res.json(await Temperature.findAll({
      limit: 100, offset: count - 100
    }));
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/types', async function (req, res, next) {
  try {
    const temperatures = await Temperature.findAll({ attributes: ['type'], limit: 100, order: [['type']], group: 'type' });
    res.json(temperatures.reverse());
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/max/:max', async function (req, res, next) {
  try {
    const temperatures = await Temperature.findAll({ limit: 3, order: [['id', 'DESC']], where: { [Op.and]: [{ value: { [Op.gte]: req.params.max } }, { type: "Simple" }] }, raw: true })
    res.json(temperatures.reverse());
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/min/:min', async function (req, res, next) {
  try {
    const temperatures = await Temperature.findAll({ limit: 3, order: [['id', 'DESC']], where: { [Op.and]: [{ value: { [Op.lte]: req.params.min } }, { type: "Simple" }] }, raw: true })
    res.json(temperatures.reverse());
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/:id', async function (req, res, next) {
  try {
    const jane = await Temperature.findOne({ where: { id: req.params.id } })
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/bytype/:type', async function (req, res, next) {
  try {
    const temperatures = await Temperature.findAll({ limit: 100, order: [['id', 'DESC']], where: { type: req.params.type } })
    res.json(temperatures.reverse());
  } catch (e) {
    res.status(400).send(e);
  }
});
router.get('/:id', async function (req, res, next) {
  try {
    const jane = await Temperature.findOne({ where: { id: req.params.id } })
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});

router.post('/', async function (req, res, next) {
  try {
    let temp = req.body;
    // console.log('Salvando Temperatura!: ' + JSON.stringify(temp));
    const jane = Temperature.build(temp);
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
    const jane = await Temperature.findOne({ where: { id: req.params.id } });
    await jane.update(temp);
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});
router.delete('/:id', async function (req, res, next) {
  try {
    const jane = await Temperature.findOne({ where: { id: req.params.id } })
    await jane.destroy();
    res.json(jane);
  } catch (e) {
    res.status(400).send(e);
  }
});
module.exports = router;