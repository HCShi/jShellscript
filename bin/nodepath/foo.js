// var foo = require('foo.js');  // 用这句话调用
// module.exports = function (n) { return n * 111 };  // console.log(foo(5));
// 这句话不能省去 moudle, 但是有了这句话以后就不能再用 exports.fun 了

exports.fun1 = function (n) { return n * 100 }  // console.log(foo.fun1(5));
exports.fun2 = function (n) { return n * 100 }  // console.log(foo.fun2(5));
// 这两句话可以同时用, 但不能跟 moudle.exports 同时用
