var createCounter = function (init) {
  var original = init;
  return {
    increment: function () {
      return ++init;
    },
    decrement: function () {
      return --init;
    },
    reset: function () {
      init = original;
      return init;
    },
  };
};

var number = 5;
counter = createCounter(number);
