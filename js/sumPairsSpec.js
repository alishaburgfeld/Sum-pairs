const sp = require("./sumPairs");

const arrayEquals = (a, b) => JSON.stringify(a) === JSON.stringify(b);

console.log(arrayEquals(sp.sumPairs([1, 2, 3, 4, 5], 9), [[4, 5]]));
console.log(arrayEquals(sp.sumPairs([1, 2, 3, 4, 5], 7), [[2, 5], [3, 4]]));
console.log(arrayEquals(sp.sumPairs([3, 1, 5, 8, 2], 27), []));
