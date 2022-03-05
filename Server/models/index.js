const Sequelize = require('sequelize');
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './database.sqlite',
  logging: false
})

require("./temperature")(sequelize);
require("./pressure")(sequelize);
(async () => {
  await sequelize.sync({ force: false });
})();
module.exports = sequelize;