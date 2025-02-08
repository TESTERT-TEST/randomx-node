const randomx = require('bindings')('randomxhash');

module.exports = {
  init: randomx.init,
  hash: (buffer) => {
    if (!Buffer.isBuffer(buffer)) {
      throw new TypeError("Expected a Buffer");
    }
    return randomx.hash(buffer);
  },
  cleanup: randomx.cleanup
};
