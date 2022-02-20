const debug = require("debug")
module.exports = class LogFactory {
    log(args) {
        debug(args);
    }
}