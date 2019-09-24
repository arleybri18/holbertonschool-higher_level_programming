#!/usr/bin/node
/* Define class Square */
const Rectangle = require('./5-square');
class Square extends Rectangle {
  /* constructor call super constructor */
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      /* instance method that print the rectangle */
      let a = this.height;
      while (a > 0) {
        console.log(c.repeat(this.width));
        a--;
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
