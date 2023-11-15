class Animal {
	constructor() {
		this.full = 1;
	}
	
	eat(amount) {
		this.full += amount;
	}
}

/*var ani = new Animal();
console.log(ani.full);
ani.eat(9);
console.log(ani.full);*/

module.exports = Animal;

if (require.main === module) {
	var ani = new Animal();
	console.log("1", ani.full);
	ani.eat(9);
	console.log("1", ani.full);
}
