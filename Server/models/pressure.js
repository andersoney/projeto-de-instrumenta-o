
module.exports = (sequelize) => {
    const moment=require("moment")
    let { Model, Sequelize, DataType } = require("sequelize")
    class Pressure extends Model { }
    Pressure.init({
        id: {
            type: Sequelize.INTEGER,
            autoIncrement: true,
            allowNull: false,
            primaryKey: true
        },
        pressure: {
            type: Sequelize.DOUBLE,
            allowNull: false
        },
        createdAt: {
            type: Sequelize.DATE,
            //note here this is the guy that you are looking for                   
            get() {
                return moment(this.getDataValue('createdAt')).format('DD/MM/YYYY h:mm:ss');
            }
        },
        updatedAt: {
            type: Sequelize.DATE,
            get() {
                return moment(this.getDataValue('updatedAt')).format('DD/MM/YYYY h:mm:ss');
            }
        }
    }, {
        hooks: {
            beforeCreate: (user, options) => {
                console.log(123);
            },
            afterCreate: (user, options) => {
                console.log(123);
            }
        },
        sequelize
    });
    module.exports = Pressure;

}