/*const Animal = require('./Animal');

var ani = new Animal();
console.log(ani.full);
ani.eat(9);
console.log(ani.full);*/

const Human = require('./human.js');

var hum = new Human();
console.log(hum.full);
console.log(hum.flag_tool);

hum.eat(9);
hum.momstouch();

console.log(hum.full);
console.log(hum.flag_tool);