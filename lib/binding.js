const path = require('path')

module.exports = require('bindings')({
  bindings: 'udx_native.node',
  name: 'udx-native-nodejs-mobile',
  module_root: path.join(__dirname, '../')
})
