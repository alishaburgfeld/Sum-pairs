const sp = require("./sumPairs");

const arrayEquals = (a, b) => JSON.stringify(a) === JSON.stringify(b);

test("should return pairs with the target sum", () => {
    expect(arrayEquals(sp.sumPairs([1, 2, 3, 4, 5], 9), [[4, 5]])).toBe(true);
    expect(arrayEquals(sp.sumPairs([1, 2, 3, 4, 5], 7), [[2, 5], [3, 4]])).toBe(true);
    expect(arrayEquals(sp.sumPairs([3, 1, 5, 8, 2], 27), [])).toBe(true);
});
