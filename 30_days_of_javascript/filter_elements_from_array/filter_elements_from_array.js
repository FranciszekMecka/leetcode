var filter = function (arr, fn) {
  resultArray = [];

  for (i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      resultArray.push(arr[i])
    }
  }
  return resultArray
};


arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }

arr = filter(arr, fn)

console.log(arr)
