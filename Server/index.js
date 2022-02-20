const LogFactory = require("./util/LogFactory");

global.log=new LogFactory();

(async () => {
    require("./config")
})();