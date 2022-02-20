const Sequelize = require('sequelize');
const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: './database.sqlite'
  })

require("./temperature")(sequelize);
require("./pressure")(sequelize);
(async () => {
    await sequelize.sync({ force: false });
})();
module.exports=sequelize;