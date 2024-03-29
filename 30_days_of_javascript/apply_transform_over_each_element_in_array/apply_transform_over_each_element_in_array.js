/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  let result = [];
  for (i = 0; i < arr.length; i++) {
    result.push(fn(arr[i], i));
  }

  return result;
};

fn = function plusone(n) {
  return n + 1;
};

arr = [1, 2, 3];
console.log(map(arr, fn));

console.log(fn(1, 2, 50));

filter_elements_from_array;
