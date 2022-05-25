/**
 * Returns an array of unique pairs of numbers from the array which sum to the given target.
 *
 * @param {Array} arr The array to be checked
 * @param {Number} target The target sum
 * @returns {Array} An array of pairs of numbers from the array which sum to the given target
 */
const sumPairs = (arr, target) => {
  const arrSet = new Set(arr);

  const result = [];
  for (const a of arrSet) {
    const b = target - a;

    if (b >= a && arrSet.has(b)) result.push([a, b]);
  }

  return result;
};

module.exports = { sumPairs };
