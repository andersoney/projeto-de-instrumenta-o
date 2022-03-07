const Sequelize = require('sequelize');
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './database.sqlite',
  logging: false
})

const Temperature = require("./temperature")(sequelize);
const Pressure = require("./pressure")(sequelize);
(async () => {
  await sequelize.sync({ force: false });
})();
module.exports = sequelize;