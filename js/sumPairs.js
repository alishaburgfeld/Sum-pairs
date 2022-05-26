/**
 * Returns an array of unique pairs of numbers from the array which sum to the given target.
 *
 * @param {Array} arr The array to be checked
 * @param {Number} target The target sum
 * @returns {Array} An array of pairs of numbers from the array which sum to the given target
 */
const sumPairs = (arr, target) => {

  // const result = new Set();

  // for (let i = 0; i < arr.length - 1; i++) {
  //   for (let j = i + 1; j < arr.length; j++) {
  //     const a = arr[i];
  //     const b = arr[j];

  //     if (a + b === target) {
  //       result.add([a, b]);
  //     }
  //   }
  // }

  // console.log(Array.from(result))

  // return Array.from(result);

  const result = [];

  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      const a = arr[i];
      const b = arr[j];


      if (a + b === target && !result.includes([a, b]) && !result.includes([b, a])) {
        result.push([a, b]);
      }
    }
  }

  return result;
};

module.exports = { sumPairs };
