#!/usr/bin/node
exports.esrever = function (list) {
  // Check if the input is an array
  if (!Array.isArray(list)) {
    return;
  }

  const reversedList = [...list];

  // Swap elements to reverse the array
  for (let i = 0; i < Math.floor(reversedList.length / 2); i++) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[reversedList.length - 1 - i];
    reversedList[reversedList.length - 1 - i] = temp;
  }

  return reversedList;
};
