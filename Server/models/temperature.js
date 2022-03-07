
module.exports = (sequelize) => {
    const moment=require("moment")
    let { Model, Sequelize, DataType } = require("sequelize")
    class Temperature extends Model { }
    Temperature.init({
        id: {
            type: Sequelize.INTEGER,
            autoIncrement: true,
            allowNull: false,
            primaryKey: true
        },
        value: {
            type: Sequelize.DOUBLE,
            allowNull: false
        },
        type:{
            type: Sequelize.STRING,
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
            },
            afterCreate: (user, options) => {
            }
        },
        sequelize
    });
    module.exports = Temperature;

}